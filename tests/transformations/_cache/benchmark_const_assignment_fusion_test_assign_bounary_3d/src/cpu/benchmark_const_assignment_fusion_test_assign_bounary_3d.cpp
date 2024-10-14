/* DaCe AUTO-GENERATED FILE. DO NOT MODIFY */
#include <dace/dace.h>
#include "../../include/hash.h"

struct benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t {

};

void __program_benchmark_const_assignment_fusion_test_assign_bounary_3d_internal(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t*__state, float * __restrict__ A, int K, int M, int N)
{

    {

        {
            #pragma omp parallel for
            for (auto t1 = 0; t1 < (Max((K - 1), (M - 1)) + 1); t1 += 1) {
                for (auto t2 = 0; t2 < (Max((M - 1), (N - 1)) + 1); t2 += 1) {
                    {
                        for (auto gsl_t1 = t1; gsl_t1 < (Max((K - 1), (M - 1)) + 1); gsl_t1 += (Max((K - 1), (M - 1)) + 1)) {
                            for (auto gsl_t2 = t2; gsl_t2 < N; gsl_t2 += N) {
                                {
                                    for (auto gsl_t1 = t1; gsl_t1 < M; gsl_t1 += M) {
                                        for (auto gsl_t2 = t2; gsl_t2 < N; gsl_t2 += N) {
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_62_8)
                                                __out = 1;
                                                ///////////////////

                                                A[((N * t1) + t2)] = __out;
                                            }
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_68_8)
                                                __out = 1;
                                                ///////////////////

                                                A[((((M * N) * (K - 1)) + (N * t1)) + t2)] = __out;
                                            }
                                        }
                                    }
                                }
                                {
                                    for (auto gsl_t1 = t1; gsl_t1 < K; gsl_t1 += K) {
                                        for (auto gsl_t2 = t2; gsl_t2 < N; gsl_t2 += N) {
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_74_8)
                                                __out = 1;
                                                ///////////////////

                                                A[(((M * N) * t1) + t2)] = __out;
                                            }
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_80_8)
                                                __out = 1;
                                                ///////////////////

                                                A[((((M * N) * t1) + (N * (M - 1))) + t2)] = __out;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    {
                        for (auto gsl_t1 = t1; gsl_t1 < K; gsl_t1 += K) {
                            for (auto gsl_t2 = t2; gsl_t2 < M; gsl_t2 += M) {
                                {
                                    float __out;

                                    ///////////////////
                                    // Tasklet code (assign_86_8)
                                    __out = 1;
                                    ///////////////////

                                    A[(((M * N) * t1) + (N * t2))] = __out;
                                }
                                {
                                    float __out;

                                    ///////////////////
                                    // Tasklet code (assign_92_8)
                                    __out = 1;
                                    ///////////////////

                                    A[(((((M * N) * t1) + (N * t2)) + N) - 1)] = __out;
                                }
                            }
                        }
                    }
                }
            }
        }

    }
}

DACE_EXPORTED void __program_benchmark_const_assignment_fusion_test_assign_bounary_3d(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, float * __restrict__ A, int K, int M, int N)
{
    __program_benchmark_const_assignment_fusion_test_assign_bounary_3d_internal(__state, A, K, M, N);
}

DACE_EXPORTED benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__dace_init_benchmark_const_assignment_fusion_test_assign_bounary_3d(int K, int M, int N)
{
    int __result = 0;
    benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state = new benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t;



    if (__result) {
        delete __state;
        return nullptr;
    }
    return __state;
}

DACE_EXPORTED int __dace_exit_benchmark_const_assignment_fusion_test_assign_bounary_3d(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state)
{
    int __err = 0;
    delete __state;
    return __err;
}
