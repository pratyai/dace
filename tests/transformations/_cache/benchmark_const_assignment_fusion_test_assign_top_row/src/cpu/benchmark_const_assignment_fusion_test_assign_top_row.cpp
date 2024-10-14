/* DaCe AUTO-GENERATED FILE. DO NOT MODIFY */
#include <dace/dace.h>
#include "../../include/hash.h"

struct benchmark_const_assignment_fusion_test_assign_top_row_state_t {

};

void __program_benchmark_const_assignment_fusion_test_assign_top_row_internal(benchmark_const_assignment_fusion_test_assign_top_row_state_t*__state, float * __restrict__ A, int M, int N)
{

    {

        {
            #pragma omp parallel for
            for (auto t = 0; t < (Max((M - 1), (N - 1)) + 1); t += 1) {
                {
                    for (auto gsl_t = t; gsl_t < N; gsl_t += N) {
                        {
                            float __out;

                            ///////////////////
                            // Tasklet code (assign_19_8)
                            __out = 1;
                            ///////////////////

                            A[t] = __out;
                        }
                        {
                            float __out;

                            ///////////////////
                            // Tasklet code (assign_25_8)
                            __out = 1;
                            ///////////////////

                            A[(t + (N * (M - 1)))] = __out;
                        }
                    }
                }
                {
                    for (auto gsl_t = t; gsl_t < M; gsl_t += M) {
                        {
                            float __out;

                            ///////////////////
                            // Tasklet code (assign_31_8)
                            __out = 1;
                            ///////////////////

                            A[(t * N)] = __out;
                        }
                        {
                            float __out;

                            ///////////////////
                            // Tasklet code (assign_37_8)
                            __out = 1;
                            ///////////////////

                            A[(((t * N) + N) - 1)] = __out;
                        }
                    }
                }
            }
        }

    }
}

DACE_EXPORTED void __program_benchmark_const_assignment_fusion_test_assign_top_row(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, float * __restrict__ A, int M, int N)
{
    __program_benchmark_const_assignment_fusion_test_assign_top_row_internal(__state, A, M, N);
}

DACE_EXPORTED benchmark_const_assignment_fusion_test_assign_top_row_state_t *__dace_init_benchmark_const_assignment_fusion_test_assign_top_row(int M, int N)
{
    int __result = 0;
    benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state = new benchmark_const_assignment_fusion_test_assign_top_row_state_t;



    if (__result) {
        delete __state;
        return nullptr;
    }
    return __state;
}

DACE_EXPORTED int __dace_exit_benchmark_const_assignment_fusion_test_assign_top_row(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state)
{
    int __err = 0;
    delete __state;
    return __err;
}
