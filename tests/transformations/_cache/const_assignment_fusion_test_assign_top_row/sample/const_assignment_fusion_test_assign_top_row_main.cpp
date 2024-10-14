#include <cstdlib>
#include "../include/const_assignment_fusion_test_assign_top_row.h"

int main(int argc, char **argv) {
    const_assignment_fusion_test_assign_top_rowHandle_t handle;
    int err;
    int M = 42;
    int N = 42;
    float * __restrict__ A = (float*) calloc((M * N), sizeof(float));


    handle = __dace_init_const_assignment_fusion_test_assign_top_row(M, N);
    __program_const_assignment_fusion_test_assign_top_row(handle, A, M, N);
    err = __dace_exit_const_assignment_fusion_test_assign_top_row(handle);

    free(A);


    return err;
}
