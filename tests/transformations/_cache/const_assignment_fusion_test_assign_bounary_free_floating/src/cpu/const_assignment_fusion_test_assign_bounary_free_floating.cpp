/* DaCe AUTO-GENERATED FILE. DO NOT MODIFY */
#include <dace/dace.h>
#include "../../include/hash.h"

struct const_assignment_fusion_test_assign_bounary_free_floating_state_t {

};

void __program_const_assignment_fusion_test_assign_bounary_free_floating_internal(const_assignment_fusion_test_assign_bounary_free_floating_state_t*__state, float * __restrict__ A, float * __restrict__ B, int M, int N)
{

    {

        {
            #pragma omp parallel for
            for (auto t = 0; t < N; t += 1) {
                {
                    float __out;

                    ///////////////////
                    // Tasklet code (assign_18_8)
                    __out = 1;
                    ///////////////////

                    A[t] = __out;
                }
                {
                    float __out;

                    ///////////////////
                    // Tasklet code (assign_31_8)
                    __out = 1;
                    ///////////////////

                    B[(t + (N * (M - 1)))] = __out;
                }
            }
        }

    }
}

DACE_EXPORTED void __program_const_assignment_fusion_test_assign_bounary_free_floating(const_assignment_fusion_test_assign_bounary_free_floating_state_t *__state, float * __restrict__ A, float * __restrict__ B, int M, int N)
{
    __program_const_assignment_fusion_test_assign_bounary_free_floating_internal(__state, A, B, M, N);
}

DACE_EXPORTED const_assignment_fusion_test_assign_bounary_free_floating_state_t *__dace_init_const_assignment_fusion_test_assign_bounary_free_floating(int M, int N)
{
    int __result = 0;
    const_assignment_fusion_test_assign_bounary_free_floating_state_t *__state = new const_assignment_fusion_test_assign_bounary_free_floating_state_t;



    if (__result) {
        delete __state;
        return nullptr;
    }
    return __state;
}

DACE_EXPORTED int __dace_exit_const_assignment_fusion_test_assign_bounary_free_floating(const_assignment_fusion_test_assign_bounary_free_floating_state_t *__state)
{
    int __err = 0;
    delete __state;
    return __err;
}
