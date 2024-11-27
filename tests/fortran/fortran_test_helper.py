import re
import subprocess
from dataclasses import dataclass, field
from os import path
from tempfile import TemporaryDirectory
from typing import Dict, Optional, Tuple, Type, Union, List, Sequence, Collection, Iterable

from fparser.common.readfortran import FortranStringReader
from fparser.two.Fortran2003 import Name
from fparser.two.parser import ParserFactory

from dace.frontend.fortran.ast_desugaring import ConstTypeInjection, ConstInstanceInjection
from dace.frontend.fortran.ast_internal_classes import Name_Node
from dace.frontend.fortran.fortran_parser import ParseConfig, create_internal_ast, SDFGConfig, \
    create_sdfg_from_internal_ast


@dataclass
class SourceCodeBuilder:
    """
    A helper class that helps to construct the source code structure for frontend tests.

    Example usage:
    ```python
    # Construct the builder, add files in the order you'd pass them to `gfortran`, (optional step) check if they all
    # compile together, then get a dictionary mapping file names (possibly auto-inferred) to their content.
    sources, main = SourceCodeBuilder().add_file('''
    module lib
    end end module lib
    ''').add_file('''
    program main
    use lib
    implicit none
    end program main
    ''').check_with_gfortran().get()
    # Then construct the SDFG.
    sdfg = create_sdfg_from_string(main, "main", sources=sources)
    ```
    """
    sources: Dict[str, str] = field(default_factory=dict)

    def add_file(self, content: str, name: Optional[str] = None):
        """Add source file contents in the order you'd pass them to `gfortran`."""
        if not name:
            name = SourceCodeBuilder._identify_name(content)
        key = f"{name}.f90"
        assert key not in self.sources, f"{key} in {list(self.sources.keys())}: {self.sources[key]}"
        self.sources[key] = content
        return self

    def check_with_gfortran(self):
        """Assert that it all compiles with `gfortran -Wall -c`."""
        with TemporaryDirectory() as td:
            # Create temporary Fortran source-file structure.
            for fname, content in self.sources.items():
                with open(path.join(td, fname), 'w') as f:
                    f.write(content)
            # Run `gfortran -Wall` to verify that it compiles.
            # Note: we're relying on the fact that python dictionaries keeps the insertion order when calling `keys()`.
            cmd = ['gfortran', '-Wall', '-shared', '-fPIC', *self.sources.keys()]

            try:
                subprocess.run(cmd, cwd=td, capture_output=True).check_returncode()
                return self
            except subprocess.CalledProcessError as e:
                print("Fortran compilation failed!")
                print(e.stderr.decode())
                raise e

    def get(self) -> Tuple[Dict[str, str], Optional[str]]:
        """Get a dictionary mapping file names (possibly auto-inferred) to their content."""
        main = None
        if 'main.f90' in self.sources:
            main = self.sources['main.f90']
        return self.sources, main

    @staticmethod
    def _identify_name(content: str) -> str:
        PPAT = re.compile("^.*\\bprogram\\b\\s*\\b(?P<prog>[a-zA-Z0-9_]+)\\b.*$", re.I | re.M | re.S)
        if PPAT.match(content):
            return 'main'
        MPAT = re.compile("^.*\\bmodule\\b\\s*\\b(?P<mod>[a-zA-Z0-9_]+)\\b.*$", re.I | re.M | re.S)
        if MPAT.match(content):
            match = MPAT.search(content)
            return match.group('mod')
        FPAT = re.compile("^.*\\bfunction\\b\\s*\\b(?P<mod>[a-zA-Z0-9_]+)\\b.*$", re.I | re.M | re.S)
        if FPAT.match(content):
            return 'main'
        SPAT = re.compile("^.*\\bsubroutine\\b\\s*\\b(?P<mod>[a-zA-Z0-9_]+)\\b.*$", re.I | re.M | re.S)
        if SPAT.match(content):
            return 'main'
        assert not any(PAT.match(content) for PAT in (PPAT, MPAT, FPAT, SPAT))


class FortranASTMatcher:
    """
    A "matcher" class that asserts if a given `node` has the right type, and its children, attributes etc. also matches
    the submatchers.

    Example usage:
    ```python
    # Construct a matcher that looks for specific patterns in the AST structure, while ignoring unnecessary details.
    m = M(Program, [
        M(Main_Program, [
            M.IGNORE(),  # program main
            M(Specification_Part),  # implicit none; double precision d(4)
            M(Execution_Part, [M(Call_Stmt)]),  # call fun(d)
            M.IGNORE(),  # end program main
        ]),
        M(Subroutine_Subprogram, [
            M(Subroutine_Stmt),  # subroutine fun(d)
            M(Specification_Part, [
                M(Implicit_Part),  # implicit none
                M(Type_Declaration_Stmt),  # double precision d(4)
            ]),
            M(Execution_Part, [M(Assignment_Stmt)]),  # d(2) = 5.5
            M(End_Subroutine_Stmt),  # end subroutine fun
        ]),
    ])
    # Check that a given Fortran AST matches that pattern.
    m.check(ast)
    ```
    """

    def __init__(self,
                 is_type: Union[None, Type, str] = None,
                 has_children: Union[None, list] = None,
                 has_attr: Optional[Dict[str, Union["FortranASTMatcher", List["FortranASTMatcher"]]]] = None,
                 has_value: Optional[str] = None):
        # TODO: Include Set[Self] to `has_children` type?
        assert not ((set() if has_attr is None else has_attr.keys())
                    & {'children'})
        self.is_type = is_type
        self.has_children = has_children
        self.has_attr = has_attr
        self.has_value = has_value

    def check(self, node):
        if self.is_type is not None:
            if isinstance(self.is_type, type):
                assert isinstance(node, self.is_type), \
                    f"type mismatch at {node}; want: {self.is_type}, got: {type(node)}"
            elif isinstance(self.is_type, str):
                assert node.__class__.__name__ == self.is_type, \
                    f"type mismatch at {node}; want: {self.is_type}, got: {type(node)}"
        if self.has_value is not None:
            assert node == self.has_value
        if self.has_children is not None and len(self.has_children) > 0:
            assert hasattr(node, 'children')
            all_children = getattr(node, 'children')
            assert len(self.has_children) == len(all_children), \
                f"#children mismatch at {node}; want: {len(self.has_children)}, got: {len(all_children)}"
            for (c, m) in zip(all_children, self.has_children):
                m.check(c)
        if self.has_attr is not None and len(self.has_attr.keys()) > 0:
            for key, subm in self.has_attr.items():
                assert hasattr(node, key)
                attr = getattr(node, key)

                if isinstance(subm, Sequence):
                    assert isinstance(attr, Sequence)
                    assert len(attr) == len(subm)
                    for (c, m) in zip(attr, subm):
                        m.check(c)
                else:
                    subm.check(attr)

    @classmethod
    def IGNORE(cls, times: Optional[int] = None) -> Union["FortranASTMatcher", List["FortranASTMatcher"]]:
        """
        A placeholder matcher to not check further down the tree.
        If `times` is `None` (which is the default), returns a single matcher.
        If `times` is an integer value, then returns a list of `IGNORE()` matchers of that size, indicating that many
        nodes on a row should be ignored.
        """
        if times is None:
            return cls()
        else:
            return [cls()] * times

    @classmethod
    def NAMED(cls, name: str):
        return cls(Name, has_attr={'string': cls(has_value=name)})


class InternalASTMatcher:
    """
    A "matcher" class that asserts if a given `node` has the right type, and its children, attributes etc. also matches
    the submatchers.

    Example usage:
    ```python
    # Construct a matcher that looks for specific patterns in the AST structure, while ignoring unnecessary details.
    m = M(Program_Node, {
        'main_program': M(Main_Program_Node, {
            'name': M(Program_Stmt_Node),
            'specification_part': M(Specification_Part_Node, {
                'specifications': [
                    M(Decl_Stmt_Node, {
                        'vardecl': [M(Var_Decl_Node)],
                    })
                ],
            }, {'interface_blocks', 'symbols', 'typedecls', 'uses'}),
            'execution_part': M(Execution_Part_Node, {
                'execution': [
                    M(Call_Expr_Node, {
                        'name': M(Name_Node),
                        'args': [M(Name_Node, {
                            'name': M(has_value='d'),
                            'type': M(has_value='DOUBLE'),
                        })],
                        'type': M(has_value='VOID'),
                    })
                ],
            }),
        }, {'parent'}),
        'structures': M(Structures, None, {'structures'}),
    }, {'function_definitions', 'module_declarations', 'modules'})
    # Check that a given internal AST matches that pattern.
    m.check(prog)
    ```
    """

    def __init__(self,
                 is_type: Optional[Type] = None,
                 has_attr: Optional[Dict[str, Union["InternalASTMatcher", List["InternalASTMatcher"], Dict[str, "InternalASTMatcher"]]]] = None,
                 has_empty_attr: Optional[Collection[str]] = None,
                 has_value: Optional[str] = None):
        # TODO: Include Set[Self] to `has_children` type?
        assert not ((set() if has_attr is None else has_attr.keys())
                    & (set() if has_empty_attr is None else has_empty_attr))
        self.is_type: Type = is_type
        self.has_attr = has_attr
        self.has_empty_attr = has_empty_attr
        self.has_value = has_value

    def check(self, node):
        if self.is_type is not None:
            assert isinstance(node, self.is_type)
        if self.has_value is not None:
            if isinstance(self.has_value, re.Pattern):
                assert self.has_value.match(node), f"{node} doesn't have value: {self.has_value}"
            else:
                assert node == self.has_value, f"{node} doesn't have value: {self.has_value}"
        if self.has_empty_attr is not None:
            for key in self.has_empty_attr:
                assert not hasattr(node, key) or not getattr(node, key), f"{node} is expected to not have key: {key}"
        if self.has_attr is not None and len(self.has_attr.keys()) > 0:
            for key, subm in self.has_attr.items():
                assert hasattr(node, key), f"{node} doesn't have key: {key}"
                attr = getattr(node, key)

                if isinstance(subm, Sequence):
                    assert isinstance(attr, Sequence), f"{attr} must be a sequence, since {subm} is."
                    assert len(attr) == len(subm), f"{attr} must have the same length as {subm}."
                    for (c, m) in zip(attr, subm):
                        m.check(c)
                elif isinstance(subm, Dict):
                    assert isinstance(attr, Dict)
                    assert len(attr) == len(subm)
                    assert subm.keys() <= attr.keys()
                    for k in subm.keys():
                        subm[k].check(attr[k])
                else:
                    subm.check(attr)

    @classmethod
    def IGNORE(cls, times: Optional[int] = None) -> Union["InternalASTMatcher", List["InternalASTMatcher"]]:
        """
        A placeholder matcher to not check further down the tree.
        If `times` is `None` (which is the default), returns a single matcher.
        If `times` is an integer value, then returns a list of `IGNORE()` matchers of that size, indicating that many
        nodes on a row should be ignored.
        """
        if times is None:
            return cls()
        else:
            return [cls()] * times

    @classmethod
    def NAMED(cls, name: Union[str, re.Pattern]):
        return cls(Name_Node, {'name': cls(has_value=name)})

    @classmethod
    def NAMED_LIKE(cls, pat: str):
        return cls.NAMED(re.compile(pat))


def create_singular_sdfg_from_string(
        sources: Dict[str, str],
        entry_point: str,
        normalize_offsets: bool = True,
        config_injections: Optional[List[ConstTypeInjection]] = None):
    entry_point = entry_point.split('.')

    cfg = ParseConfig(main=sources['main.f90'], sources=sources, entry_points=tuple(entry_point),
                      config_injections=config_injections)
    own_ast, program = create_internal_ast(cfg)

    cfg = SDFGConfig({entry_point[-1]: entry_point}, config_injections=config_injections,
                     normalize_offsets=normalize_offsets, multiple_sdfgs=False)
    gmap = create_sdfg_from_internal_ast(own_ast, program, cfg)
    assert gmap.keys() == {entry_point[-1]}
    g = list(gmap.values())[0]

    return g


def test_stubgen():
    NAME, COUNTER = 'stub', 0

    def _stub_fn(args: Iterable[str]) -> Tuple[str, str]:
        nonlocal COUNTER
        fname, COUNTER = f"{NAME}_{COUNTER}", COUNTER + 1

        ARGNAME, ARGC = 'a', 0
        arg_decls = []
        for a in args:
            aname, ARGC = f"{ARGNAME}_{ARGC}", ARGC + 1
            dims: re.Match = re.search(r'(\([^)]*\))', a, re.IGNORECASE)
            if dims:
                dims: str = dims.group(1)
            else:
                dims: str = ''
            atype = a.removesuffix(dims)
            if atype == 'CHARACTER':
                atype = 'CHARACTER(LEN = *)'
            elif atype == 'SHORT':
                atype = 'INTEGER(SELECTED_INT_KIND(4))'
            elif atype == 'BYTE':
                atype = 'INTEGER(SELECTED_INT_KIND(1))'
            arg_decls.append((aname, f"{atype}, intent(in) :: {aname}{dims}"))
        fdef = f"""
function {fname}({', '.join([d for d, _ in arg_decls] + ['start', 'count'])})
  {'\n'.join([d for _, d in arg_decls])}
  integer, optional :: start(:), count(:)
  integer :: {fname}
  {fname} = nf90_noerr
end function {fname}
"""
        return fname, fdef

    R, D, I, S, B, C = 'REAL', 'DOUBLE PRECISION', 'INTEGER', 'SHORT', 'BYTE', 'CHARACTER'
    RV, DV, IV, CV = tuple(t + '(:)' for t in (R, D, I, C))
    RM, DM, IM, CM = tuple(t + '(:, :)' for t in (R, D, I, C))
    RH, DH, IH, CH = tuple(t + '(:, :, :)' for t in (R, D, I, C))
    RH4, DH4, IH4, CH4 = tuple(t + '(:, :, :, :)' for t in (R, D, I, C))
    argsets: Set[Tuple[str, ...]] = (
            {(I, I, t) for t in [R, D, I, C, RV, DV, IV, CV, RM, DM, IM, CM, RH, DH, IH, RH4, DH4]}
            | {(I, I, C, C), (I, I, CV, CV), (I, I, C, I), (I, I, C, R), (I, I, C, D), (I, I, C, S), (I, I, C, B)}
            | {(I, C, I, IV, I)})
    stubs = [_stub_fn(a) for a in argsets]

    nf90_consts = """
  integer, parameter :: nf90_noerr = 0
  integer, parameter :: nf90_nowrite = 0
  integer, parameter :: nf90_clobber = 0
  integer, parameter :: nf90_max_var_dims = 0
  integer, parameter :: nf90_enotvar = 0
  integer, parameter :: nf90_global = 0
  integer, parameter :: nf90_double = 0
  integer, parameter :: nf90_float = 0
  integer, parameter :: nf90_byte = 0
  integer, parameter :: nf90_int = 0
  integer, parameter :: nf90_short = 0
"""
    nf90_fns = {'nf90_get_var', 'nf90_put_var', 'nf90_def_var', 'nf90_get_att', 'nf90_put_att'}
    mprocs = [f"module procedure {f}" for f, _ in stubs]
    nf90_ifcs = [f"""
interface {f}
{'\n'.join(mprocs)}
end interface {f}
""" for f in nf90_fns]

    mdef = f"""
module netcdf
implicit none
{nf90_consts}
{'\n'.join(nf90_ifcs)}
contains
{'\n'.join([f for _, f in stubs])}
  function nf90_open(path, mode, ncid, chunksize)
    character(LEN=*), intent(IN) :: path
    integer, intent(IN) :: mode
    integer, intent(OUT) :: ncid
    integer, optional, intent(INOUT) :: chunksize
    integer :: nf90_open
    nf90_open = nf90_noerr
  end function nf90_open
  function nf90_create(path, cmode, ncid, initialsize, chunksize)
    character(LEN=*), intent(IN) :: path
    integer, intent(IN) :: cmode
    integer, intent(OUT) :: ncid
    integer, optional, intent(IN) :: initialsize
    integer, optional, intent(INOUT) :: chunksize
    integer :: nf90_create
    nf90_create = nf90_noerr
  end function nf90_create
  function nf90_strerror(ncerr)
    character(LEN=80) :: nf90_strerror
    integer, intent(IN) :: ncerr
    nf90_strerror = "!"
  end function nf90_strerror
  function nf90_close(ncid)
    integer, intent(IN) :: ncid
    integer :: nf90_close
    nf90_close = nf90_noerr
  end function nf90_close
  function nf90_enddef(ncid, h_minfree, v_align, v_minfree, r_align)
    integer, intent(IN) :: ncid
    integer, optional, intent(IN) :: h_minfree, v_align, v_minfree, r_align
    integer :: nf90_enddef
    nf90_enddef = nf90_noerr
  end function nf90_enddef
  function nf90_inq_varid(ncid, name, varid)
    integer, intent(IN) :: ncid
    character(LEN=*), intent(IN) :: name
    integer, intent(OUT) :: varid
    integer :: nf90_inq_varid
    nf90_inq_varid = nf90_noerr
  end function nf90_inq_varid
  function nf90_inquire_variable(ncid, varid, name, xtype, ndims, dimids, nAtts)
    integer, intent(IN) :: ncid, varid
    character(LEN=*), optional, intent(OUT) :: name
    integer, optional, intent(OUT) :: xtype, ndims
    integer, dimension(:), optional, intent(OUT) :: dimids
    integer, optional, intent(OUT) :: nAtts
    integer :: nf90_inquire_variable
    nf90_inquire_variable = nf90_noerr
  end function nf90_inquire_variable
  function nf90_inquire_dimension(ncid, dimid, name, len)
    integer, intent(IN) :: ncid, dimid
    character(LEN=*), optional, intent(OUT) :: name
    integer, optional, intent(OUT) :: len
    integer :: nf90_inquire_dimension
    nf90_inquire_dimension = nf90_noerr
  end function nf90_inquire_dimension
  function nf90_inquire_attribute(ncid, varid, name, xtype, len, attnum)
    integer, intent(in)           :: ncid, varid
    character(len=*), intent(in)           :: name
    integer, intent(out), optional :: xtype, len, attnum
    integer                                    :: nf90_inquire_attribute
    nf90_inquire_attribute = nf90_noerr
  end function nf90_inquire_attribute
  function nf90_inq_dimid(ncid, name, dimid)
    integer, intent(in) :: ncid
    character(len=*), intent(in) :: name
    integer, intent(out) :: dimid
    integer                          :: nf90_inq_dimid
    nf90_inq_dimid = nf90_noerr
  end function nf90_inq_dimid
  function nf90_inq_attname(ncid, varid, attnum, name)
    integer,             intent( in) :: ncid, varid, attnum
    character (len = *), intent(out) :: name
    integer                          :: nf90_inq_attname
    nf90_inq_attname = nf90_noerr
  end function nf90_inq_attname
  function nf90_def_dim(ncid, name, len, dimid)
    integer,             intent( in) :: ncid
    character (len = *), intent( in) :: name
    integer,             intent( in) :: len
    integer,             intent(out) :: dimid
    integer                          :: nf90_def_dim
    nf90_def_dim = nf90_noerr
  end function nf90_def_dim
  function nf90_copy_att(ncid_in, varid_in, name, ncid_out, varid_out)
    integer,             intent( in) :: ncid_in,  varid_in
    character (len = *), intent( in) :: name
    integer,             intent( in) :: ncid_out, varid_out
    integer                          :: nf90_copy_att
    nf90_copy_att = nf90_noerr
  end function nf90_copy_att
end module netcdf
"""
    # with open('/Users/pmz/Downloads/stub.f90', 'w') as f:
    #     f.write(mdef)
    parser = ParserFactory().create(std="f2008")
    ast = parser(FortranStringReader(mdef))
    with open('/Users/pmz/Downloads/stub.f90', 'w') as f:
        f.write(ast.tofortran())
