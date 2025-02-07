# Copyright 2019-2023 ETH Zurich and the DaCe authors. All rights reserved.

import numpy as np
import pytest

import dace
from dace import dtypes
from dace.frontend.fortran import fortran_parser
from dace.frontend.fortran.fortran_parser import create_singular_sdfg_from_string
from tests.fortran.fortran_test_helper import SourceCodeBuilder, deduce_f2dace_variables_for_array


def test_fortran_frontend_bit_size():
    test_string = """
                    PROGRAM intrinsic_math_test_bit_size
                    implicit none
                    integer, dimension(4) :: res
                    CALL intrinsic_math_test_bit_size_function(res)
                    end

                    SUBROUTINE intrinsic_math_test_bit_size_function(res)
                    integer, dimension(4) :: res
                    logical :: a = .TRUE.
                    integer :: b = 1
                    real :: c = 1
                    double precision :: d = 1

                    res(1) = BIT_SIZE(a)
                    res(2) = BIT_SIZE(b)
                    res(3) = BIT_SIZE(c)
                    res(4) = BIT_SIZE(d)

                    END SUBROUTINE intrinsic_math_test_bit_size_function
                    """

    sdfg = fortran_parser.create_sdfg_from_string(test_string, "intrinsic_math_test_bit_size", True)
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 4
    res = np.full([size], 42, order="F", dtype=np.int32)
    sdfg(res=res)

    assert np.allclose(res, [32, 32, 32, 64])


def test_fortran_frontend_bit_size_symbolic():
    sources, main = SourceCodeBuilder().add_file("""
subroutine main(arrsize, arrsize2, arrsize3, res, res2, res3)
  implicit none
  integer :: arrsize
  integer :: arrsize2
  integer :: arrsize3
  integer :: res(arrsize)
  integer :: res2(arrsize, arrsize2, arrsize3)
  integer :: res3(arrsize + arrsize2, arrsize2*5, arrsize3 + arrsize2*arrsize)

  res(1) = size(res)
  res(2) = size(res2)
  res(3) = size(res3)
  res(4) = size(res)*2
  res(5) = size(res)*size(res2)*size(res3)
  res(6) = size(res2, 1) + size(res2, 2) + size(res2, 3)
  res(7) = size(res3, 1) + size(res3, 2) + size(res3, 3)
end subroutine main
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 24
    size2 = 5
    size3 = 7
    res = np.full([size], 42, order="F", dtype=np.int32)
    res2 = np.full([size, size2, size3], 42, order="F", dtype=np.int32)
    res3 = np.full([size + size2, size2 * 5, size3 + size * size2], 42, order="F", dtype=np.int32)
    sdfg(res=res, res2=res2, res3=res3, arrsize=size, arrsize2=size2, arrsize3=size3)

    assert res[0] == size
    assert res[1] == size * size2 * size3
    assert res[2] == (size + size2) * (size2 * 5) * (size3 + size2 * size)
    assert res[3] == size * 2
    assert res[4] == res[0] * res[1] * res[2]
    assert res[5] == size + size2 + size3
    assert res[6] == size + size2 + size2 * 5 + size3 + size * size2


def test_fortran_frontend_size_arbitrary():
    sources, main = SourceCodeBuilder().add_file("""
subroutine main(res)
  implicit none
  integer :: res(:, :)
  res(1, 1) = size(res)
  res(2, 1) = size(res, 1)
  res(3, 1) = size(res, 2)
end subroutine main
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 7
    size2 = 5
    res = np.full([size, size2], 42, order="F", dtype=np.int32)
    sdfg(res=res, **deduce_f2dace_variables_for_array(res, 'res', 0),
         arrsize=size, arrsize2=size2)
    print(res)

    assert res[0, 0] == size * size2
    assert res[1, 0] == size
    assert res[2, 0] == size2


def test_fortran_frontend_present():
    sources, main = SourceCodeBuilder().add_file("""
subroutine main(res, res2, a)
  integer, dimension(4) :: res
  integer, dimension(4) :: res2
  integer :: a
  call tf2(res, a=a)
  call tf2(res2)

contains

  subroutine tf2(res, a)
    integer, dimension(4) :: res
    integer, optional :: a
    res(1) = present(a)
  end subroutine tf2
end subroutine
""", 'main').check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'main')
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 4
    res = np.full([size], 42, order="F", dtype=np.int32)
    res2 = np.full([size], 42, order="F", dtype=np.int32)
    sdfg(res=res, res2=res2, a=5)

    assert res[0] == 1
    assert res2[0] == 0


def test_fortran_frontend_bitwise_ops():
    sources, main = SourceCodeBuilder().add_file("""
    SUBROUTINE bitwise_ops(inp, res)

    integer, dimension(11) :: inp
    integer, dimension(11) :: res

    res(1) = IBSET(inp(1), 0)
    res(2) = IBSET(inp(2), 30)

    res(3) = IBCLR(inp(3), 0)
    res(4) = IBCLR(inp(4), 30)

    res(5) = IEOR(inp(5), 63)
    res(6) = IEOR(inp(6), 480)

    res(7) = ISHFT(inp(7), 5)
    res(8) = ISHFT(inp(8), 30)

    res(9) = ISHFT(inp(9), -5)
    res(10) = ISHFT(inp(10), -30)

    res(11) = ISHFT(inp(11), 0)

    END SUBROUTINE bitwise_ops
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'bitwise_ops', normalize_offsets=True)
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 11
    inp = np.full([size], 42, order="F", dtype=np.int32)
    inp[:] = [32, 32, 33, 1073741825, 53, 530, 12, 1, 128, 1073741824, 12]

    res = np.full([size], 42, order="F", dtype=np.int32)

    sdfg(inp=inp, res=res)

    assert np.allclose(res, [33, 1073741856, 32, 1, 10, 1010, 384, 1073741824, 4, 1, 12])


def test_ieor():
    sources, main = SourceCodeBuilder().add_file("""
MODULE random_numbers_mix
  IMPLICIT NONE
  SAVE
  INTEGER(KIND = 4), PARAMETER :: jpq = 607
  TYPE :: randomnumberstream
    INTEGER(KIND = 4) :: iused
    INTEGER(KIND = 4) :: inittest
    INTEGER(KIND = 4), DIMENSION(607) :: ix
    REAL(KIND = 8) :: zrm
  END TYPE randomnumberstream
  CONTAINS
  SUBROUTINE initialize_random_numbers(kseed, yd_stream_var_101)
    INTEGER(KIND = 4), INTENT(IN) :: kseed
    TYPE(randomnumberstream), INTENT(INOUT) :: yd_stream_var_101
    INTEGER(KIND = 4) :: idum, jj_var_102, jbit
    REAL(KIND = 8), DIMENSION(999) :: zwarmup
    idum = ABS(IEOR(kseed, 123459876))
    IF (idum == 0) idum = 123459876
    DO jj_var_102 = 1, 64
      IF (BTEST(idum, 31)) THEN
        idum = IBSET(ISHFT(IEOR(idum, 87), 1), 0)
      ELSE
        idum = IBCLR(ISHFT(idum, 1), 0)
      END IF
    END DO
    yd_stream_var_101 % ix(1 : 606) = 0
    yd_stream_var_101 % ix(2) = ISHFT(IBITS(idum, 0, 29), 1)
    yd_stream_var_101 % ix(jpq) = IBITS(idum, 29, BIT_SIZE(idum) + 1 - 30)
    DO jbit = 1, 29
      DO jj_var_102 = 3, 606
        IF (BTEST(idum, 31)) THEN
          idum = IBSET(ISHFT(IEOR(idum, 87), 1), 0)
          yd_stream_var_101 % ix(jj_var_102) = IBSET(yd_stream_var_101 % ix(jj_var_102), jbit)
        ELSE
          idum = IBCLR(ISHFT(idum, 1), 0)
        END IF
      END DO
    END DO
    yd_stream_var_101 % ix(502) = IBSET(yd_stream_var_101 % ix(502), 0)
    yd_stream_var_101 % iused = 607
    yd_stream_var_101 % zrm = 9.313225746154785D-10
    yd_stream_var_101 % inittest = 12345678
    CALL uniform_distribution(zwarmup, yd_stream_var_101)
  END SUBROUTINE initialize_random_numbers
  SUBROUTINE uniform_distribution(px, yd_stream_var_103)
    TYPE(randomnumberstream), INTENT(INOUT) :: yd_stream_var_103
    REAL(KIND = 8), DIMENSION(:), INTENT(OUT) :: px
    INTEGER(KIND = 4) :: jj_var_104, jk_var_105, in_var_106, ifilled
    in_var_106 = SIZE(px)
    ifilled = 0
    DO jj_var_104 = yd_stream_var_103 % iused + 1, MIN(607, in_var_106 + yd_stream_var_103 % iused)
      px(jj_var_104 - yd_stream_var_103 % iused) = yd_stream_var_103 % ix(jj_var_104) * yd_stream_var_103 % zrm
      ifilled = ifilled + 1
    END DO
    yd_stream_var_103 % iused = yd_stream_var_103 % iused + ifilled
    IF (ifilled == in_var_106) THEN
      RETURN
    END IF
    DO WHILE (ifilled < in_var_106)
      DO jj_var_104 = 1, 273
        yd_stream_var_103 % ix(jj_var_104) = IAND(1073741823, yd_stream_var_103 % ix(jj_var_104) + yd_stream_var_103 % ix(jj_var_104 - 273 + 607))
      END DO
      DO jk_var_105 = 1, 2
        DO jj_var_104 = 274 + (jk_var_105 - 1) * 167, MIN(607, 273 + jk_var_105 * 167)
          yd_stream_var_103 % ix(jj_var_104) = IAND(1073741823, yd_stream_var_103 % ix(jj_var_104) + yd_stream_var_103 % ix(jj_var_104 - 273))
        END DO
      END DO
      yd_stream_var_103 % iused = MIN(607, in_var_106 - ifilled)
      px(ifilled + 1 : ifilled + yd_stream_var_103 % iused) = yd_stream_var_103 % ix(1 : yd_stream_var_103 % iused) * yd_stream_var_103 % zrm
      ifilled = ifilled + yd_stream_var_103 % iused
    END DO
  END SUBROUTINE uniform_distribution
END MODULE random_numbers_mix

subroutine main(k)
  use random_numbers_mix
  integer, intent(in) :: k
  type(randomnumberstream) :: o
  call initialize_random_numbers(k, o)
end subroutine main
""").check_with_gfortran().get()
    g = create_singular_sdfg_from_string(sources, 'main')
    g.save('/Users/pmz/Downloads/bleh.sdfg')
    g.simplify(verbose=True)
    g = g.compile()

    g(k=1)


def test_fortran_frontend_bitwise_ops2():
    sources, main = SourceCodeBuilder().add_file("""
    SUBROUTINE bitwise_ops(inp, res)

    integer, dimension(6) :: inp
    integer, dimension(6) :: res

    res(1) = IAND(inp(1), 0)
    res(2) = IAND(inp(2), 31)

    res(3) = BTEST(inp(3), 0)
    res(4) = BTEST(inp(4), 5)

    res(5) = IBITS(inp(5), 0, 5)
    res(6) = IBITS(inp(6), 3, 10)

    END SUBROUTINE bitwise_ops
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'bitwise_ops', normalize_offsets=True)
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 6
    inp = np.full([size], 42, order="F", dtype=np.int32)
    inp[:] = [2147483647, 16, 3, 31, 30, 630]

    res = np.full([size], 42, order="F", dtype=np.int32)

    sdfg(inp=inp, res=res)

    assert np.allclose(res, [0, 16, 1, 0, 30, 78])


def test_fortran_frontend_allocated():
    # FIXME: this pattern is generally not supported.
    # this needs an update once defered allocs are merged

    sources, main = SourceCodeBuilder().add_file("""
    SUBROUTINE allocated_test(res)

    integer, allocatable, dimension(:) :: data
    integer, dimension(3) :: res

    res(1) = ALLOCATED(data)

    ALLOCATE(data(6))

    res(2) = ALLOCATED(data)

    DEALLOCATE(data)

    res(3) = ALLOCATED(data)

    END SUBROUTINE allocated_test
""").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'allocated_test', normalize_offsets=True)
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 3
    res = np.full([size], 42, order="F", dtype=np.int32)

    sdfg(res=res)

    assert np.allclose(res, [0, 1, 0])


def test_fortran_frontend_allocated_nested():
    # FIXME: this pattern is generally not supported.
    # this needs an update once defered allocs are merged

    sources, main = SourceCodeBuilder().add_file("""
    MODULE allocated_test_interface
        INTERFACE
            SUBROUTINE allocated_test_nested(data, res)
                integer, allocatable, dimension(:) :: data
                integer, dimension(3) :: res
            END SUBROUTINE allocated_test_nested
        END INTERFACE
    END MODULE

    SUBROUTINE allocated_test(res)
    USE allocated_test_interface
    implicit none
    integer, allocatable, dimension(:) :: data
    integer, dimension(3) :: res

    res(1) = ALLOCATED(data)

    ALLOCATE(data(6))

    CALL allocated_test_nested(data, res)

    END SUBROUTINE allocated_test

    SUBROUTINE allocated_test_nested(data, res)

    integer, allocatable, dimension(:) :: data
    integer, dimension(3) :: res

    res(2) = ALLOCATED(data)

    DEALLOCATE(data)

    res(3) = ALLOCATED(data)

    END SUBROUTINE allocated_test_nested
""", 'main').check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'allocated_test', normalize_offsets=True)
    sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 3
    res = np.full([size], 42, order="F", dtype=np.int32)

    sdfg(res=res)

    assert np.allclose(res, [0, 1, 0])


@pytest.mark.skip(reason="Needs suport for allocatable + datarefs")
def test_fortran_frontend_allocated_struct():
    # FIXME: this pattern is generally not supported.
    # this needs an update once defered allocs are merged

    sources, main = SourceCodeBuilder().add_file("""
    MODULE allocated_test_interface
        IMPLICIT NONE

        TYPE array_container
            integer, allocatable, dimension(:) :: data
        END TYPE array_container

    END MODULE

    SUBROUTINE allocated_test(res)
    USE allocated_test_interface
    implicit none

    type(array_container) :: container
    integer, dimension(3) :: res

    res(1) = ALLOCATED(container%data)

    ALLOCATE(container%data(6))

    res(2) = ALLOCATED(container%data)

    DEALLOCATE(container%data)

    res(3) = ALLOCATED(container%data)

    END SUBROUTINE allocated_test
""", "main").check_with_gfortran().get()
    sdfg = create_singular_sdfg_from_string(sources, 'allocated_test', normalize_offsets=True)
    # sdfg.simplify(verbose=True)
    sdfg.compile()

    size = 3
    res = np.full([size], 42, order="F", dtype=np.int32)

    sdfg(res=res)

    assert np.allclose(res, [0, 1, 0])


if __name__ == "__main__":
    test_fortran_frontend_bit_size()
    test_fortran_frontend_bit_size_symbolic()
    test_fortran_frontend_size_arbitrary()
    test_fortran_frontend_present()
    test_fortran_frontend_bitwise_ops()
    test_fortran_frontend_bitwise_ops2()
    test_fortran_frontend_allocated()
    test_fortran_frontend_allocated_nested()
    # FIXME: ALLOCATED does not support data refs
    # test_fortran_frontend_allocated_struct()
