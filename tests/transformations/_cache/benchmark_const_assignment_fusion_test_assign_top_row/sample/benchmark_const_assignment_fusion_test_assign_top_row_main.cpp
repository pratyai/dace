#include <cstdlib>
#include "../include/benchmark_const_assignment_fusion_test_assign_top_row.h"

int main(int argc, char **argv) {
    benchmark_const_assignment_fusion_test_assign_top_rowHandle_t handle;
    int err;
    int M = 42;
    int N = 42;
    float * __restrict__ A = (float*) calloc((M * N), sizeof(float));


    handle = __dace_init_benchmark_const_assignment_fusion_test_assign_top_row(M, N);
    __program_benchmark_const_assignment_fusion_test_assign_top_row(handle, A, M, N);
    err = __dace_exit_benchmark_const_assignment_fusion_test_assign_top_row(handle);

    free(A);


    return err;
}
