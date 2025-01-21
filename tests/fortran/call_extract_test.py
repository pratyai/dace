# Copyright 2019-2023 ETH Zurich and the DaCe authors. All rights reserved.

import numpy as np
import pytest

from dace.frontend.fortran import fortran_parser
from dace.frontend.fortran.fortran_parser import create_singular_sdfg_from_string
from tests.fortran.fortran_test_helper import SourceCodeBuilder


def test_fortran_frontend_call_extract():
    sources, main = SourceCodeBuilder().add_file("""
subroutine main(d, res)
  implicit none
  real, dimension(2) :: d
  real, dimension(2) :: res
  res(1) = sqrt(sign(exp(d(1)), log(d(1))))
  res(2) = min(sqrt(exp(d(1))), sqrt(exp(d(1))) - 1)
end subroutine main
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.save('/Users/pmz/Downloads/bleh.sdfg')
    sdfg.simplify(verbose=True)
    sdfg.save('/Users/pmz/Downloads/bleh2.sdfg')
    sdfg.compile()
    
    d = np.full([2], 42, order="F", dtype=np.float32)
    res = np.full([2], 42, order="F", dtype=np.float32)
    sdfg(d=d, res=res)
    assert np.allclose(res, [np.sqrt(np.exp(d[0])), np.sqrt(np.exp(d[0])) - 1])


if __name__ == "__main__":

    test_fortran_frontend_call_extract()
