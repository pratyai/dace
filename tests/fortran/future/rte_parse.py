from dace.frontend.fortran.fortran_parser import create_sdfg_from_string


def test_kind():
    prog = """
program main
    implicit none
    integer :: x1 = kind(.true.)
    integer :: x2 = kind(1)
    integer :: x3 = kind(1.0)
    integer :: x4 = kind(1.d0)
    integer :: x5 = kind('cab')
end program main
"""
    g = create_sdfg_from_string(prog, 'prog')
    g.validate()
    g.save('/Users/pmz/Downloads/4tran/test_kind.sdfg')
    g.compile()
