# Copyright 2023 ETH Zurich and the DaCe authors. All rights reserved.

import numpy as np

from dace.frontend.fortran import fortran_parser
from tests.fortran.fotran_test_helper import SourceCodeBuilder, create_singular_sdfg_from_string


def test_fortran_frontend_rename():
    """
    Tests that the Fortran frontend can parse complex initializations.
    """
    sources, main = SourceCodeBuilder().add_file("""
module lib
  implicit none
  integer, parameter :: pi4 = 9
  integer, parameter :: i4 = selected_int_kind(pi4)
end module lib
""").add_file("""
subroutine main(d)
  use lib, only: ik4 => i4
  implicit none
  double precision d(4)
  integer(ik4) :: i

  i = 4
  d(2) = 5.5 + i
end subroutine main
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.simplify(verbose=True)
    a = np.full([4], 42, order="F", dtype=np.float64)
    sdfg(d=a)
    assert (a[0] == 42)
    assert (a[1] == 9.5)
    assert (a[2] == 42)


if __name__ == "__main__":
    test_fortran_frontend_rename()
