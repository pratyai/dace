#include <dace/dace.h>
typedef void * const_assignment_fusion_test_assign_top_rowHandle_t;
extern "C" const_assignment_fusion_test_assign_top_rowHandle_t __dace_init_const_assignment_fusion_test_assign_top_row(int M, int N);
extern "C" int __dace_exit_const_assignment_fusion_test_assign_top_row(const_assignment_fusion_test_assign_top_rowHandle_t handle);
extern "C" void __program_const_assignment_fusion_test_assign_top_row(const_assignment_fusion_test_assign_top_rowHandle_t handle, float * __restrict__ A, int M, int N);
