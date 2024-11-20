# Copyright 2023 ETH Zurich and the DaCe authors. All rights reserved.

import numpy as np

from tests.fortran.fotran_test_helper import create_singular_sdfg_from_string, SourceCodeBuilder


def test_fortran_frontend_global():
    """
    Tests that the Fortran frontend can parse complex global includes.
    """
    sources, main = SourceCodeBuilder().add_file("""
module global_lib
  implicit none
  type simple_type
    double precision, pointer :: w(:, :, :)
    integer a
  end type simple_type
  integer :: outside_init = 1
end module global_lib
""").add_file("""
module nested_two
  implicit none
contains
  subroutine nestedtwo(i)
    use global_lib, only: outside_init
    integer :: i

    i = outside_init + 1
  end subroutine nestedtwo
end module nested_two
""").add_file("""
module nested_one
  implicit none
contains
  subroutine nested(i, a)
    use nested_two, only: nestedtwo
    integer :: i
    double precision :: a(:, :, :)

    i = 0
    call nestedtwo(i)
    a(i + 1, i + 1, i + 1) = 5.5
  end subroutine nested
end module nested_one
""").add_file("""
subroutine main(d)
  use global_lib, only: outside_init, simple_type
  use nested_one, only: nested
  double precision d(4)
  double precision :: a(4, 4, 4)
  integer :: i
  type(simple_type) :: ptr_patch

  ptr_patch%w(:, :, :) = 5.5
  i = outside_init
  call nested(i, ptr_patch%w)
  d(i + 1) = 5.5 + ptr_patch%w(3, 3, 3)
end subroutine main
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.simplify(verbose=True)
    # sdfg.compile()

    # a = np.full([4], 42, order="F", dtype=np.float64)
    # a2 = np.full([4, 4, 4], 42, order="F", dtype=np.float64)

    # TODO Add validation - but we need python structs for this.
    # sdfg(d=a,a=a2)
    # assert (a[0] == 42)
    # assert (a[1] == 5.5)
    # assert (a[2] == 42)


if __name__ == "__main__":
    test_fortran_frontend_global()
