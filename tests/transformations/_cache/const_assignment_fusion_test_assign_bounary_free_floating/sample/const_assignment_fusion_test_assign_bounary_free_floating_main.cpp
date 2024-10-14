#include <cstdlib>
#include "../include/const_assignment_fusion_test_assign_bounary_free_floating.h"

int main(int argc, char **argv) {
    const_assignment_fusion_test_assign_bounary_free_floatingHandle_t handle;
    int err;
    int M = 42;
    int N = 42;
    float * __restrict__ A = (float*) calloc((M * N), sizeof(float));
    float * __restrict__ B = (float*) calloc((M * N), sizeof(float));


    handle = __dace_init_const_assignment_fusion_test_assign_bounary_free_floating(M, N);
    __program_const_assignment_fusion_test_assign_bounary_free_floating(handle, A, B, M, N);
    err = __dace_exit_const_assignment_fusion_test_assign_bounary_free_floating(handle);

    free(A);
    free(B);


    return err;
}
