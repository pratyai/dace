#include <cstdlib>
#include "../include/benchmark_const_assignment_fusion_test_assign_bounary_3d.h"

int main(int argc, char **argv) {
    benchmark_const_assignment_fusion_test_assign_bounary_3dHandle_t handle;
    int err;
    int K = 42;
    int M = 42;
    int N = 42;
    float * __restrict__ A = (float*) calloc(((K * M) * N), sizeof(float));


    handle = __dace_init_benchmark_const_assignment_fusion_test_assign_bounary_3d(K, M, N);
    __program_benchmark_const_assignment_fusion_test_assign_bounary_3d(handle, A, K, M, N);
    err = __dace_exit_benchmark_const_assignment_fusion_test_assign_bounary_3d(handle);

    free(A);


    return err;
}
