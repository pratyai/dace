
#include <cuda_runtime.h>
#include <dace/dace.h>


struct benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t {
    dace::cuda::Context *gpu_context;
};



DACE_EXPORTED int __dace_init_cuda(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, int K, int M, int N);
DACE_EXPORTED int __dace_exit_cuda(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state);



int __dace_init_cuda(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, int K, int M, int N) {
    int count;

    // Check that we are able to run cuda code
    if (cudaGetDeviceCount(&count) != cudaSuccess)
    {
        printf("ERROR: GPU drivers are not configured or cuda-capable device "
               "not found\n");
        return 1;
    }
    if (count == 0)
    {
        printf("ERROR: No cuda-capable devices found\n");
        return 2;
    }

    // Initialize cuda before we run the application
    float *dev_X;
    DACE_GPU_CHECK(cudaMalloc((void **) &dev_X, 1));
    DACE_GPU_CHECK(cudaFree(dev_X));

    

    __state->gpu_context = new dace::cuda::Context(3, 5);

    // Create cuda streams and events
    for(int i = 0; i < 3; ++i) {
        DACE_GPU_CHECK(cudaStreamCreateWithFlags(&__state->gpu_context->internal_streams[i], cudaStreamNonBlocking));
        __state->gpu_context->streams[i] = __state->gpu_context->internal_streams[i]; // Allow for externals to modify streams
    }
    for(int i = 0; i < 5; ++i) {
        DACE_GPU_CHECK(cudaEventCreateWithFlags(&__state->gpu_context->events[i], cudaEventDisableTiming));
    }

    

    return 0;
}

int __dace_exit_cuda(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state) {
    

    // Synchronize and check for CUDA errors
    int __err = static_cast<int>(__state->gpu_context->lasterror);
    if (__err == 0)
        __err = static_cast<int>(cudaDeviceSynchronize());

    // Destroy cuda streams and events
    for(int i = 0; i < 3; ++i) {
        DACE_GPU_CHECK(cudaStreamDestroy(__state->gpu_context->internal_streams[i]));
    }
    for(int i = 0; i < 5; ++i) {
        DACE_GPU_CHECK(cudaEventDestroy(__state->gpu_context->events[i]));
    }

    delete __state->gpu_context;
    return __err;
}

DACE_EXPORTED bool __dace_gpu_set_stream(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, int streamid, gpuStream_t stream)
{
    if (streamid < 0 || streamid >= 3)
        return false;

    __state->gpu_context->streams[streamid] = stream;

    return true;
}

DACE_EXPORTED void __dace_gpu_set_all_streams(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, gpuStream_t stream)
{
    for (int i = 0; i < 3; ++i)
        __state->gpu_context->streams[i] = stream;
}

__global__ void __launch_bounds__(32) map_fusion_wrapper_0_0_15(float * __restrict__ gpu_A, int K, int M, int N) {
    {
        {
            int t2 = (blockIdx.x * 32 + threadIdx.x);
            int t1 = (blockIdx.y * 1 + threadIdx.y);
            if (t2 < (Max((M - 1), (N - 1)) + 1)) {
                {
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

                                                gpu_A[((N * t1) + t2)] = __out;
                                            }
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_68_8)
                                                __out = 1;
                                                ///////////////////

                                                gpu_A[((((M * N) * (K - 1)) + (N * t1)) + t2)] = __out;
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

                                                gpu_A[(((M * N) * t1) + t2)] = __out;
                                            }
                                            {
                                                float __out;

                                                ///////////////////
                                                // Tasklet code (assign_80_8)
                                                __out = 1;
                                                ///////////////////

                                                gpu_A[((((M * N) * t1) + (N * (M - 1))) + t2)] = __out;
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

                                    gpu_A[(((M * N) * t1) + (N * t2))] = __out;
                                }
                                {
                                    float __out;

                                    ///////////////////
                                    // Tasklet code (assign_92_8)
                                    __out = 1;
                                    ///////////////////

                                    gpu_A[(((((M * N) * t1) + (N * t2)) + N) - 1)] = __out;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


DACE_EXPORTED void __dace_runkernel_map_fusion_wrapper_0_0_15(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, float * __restrict__ gpu_A, int K, int M, int N);
void __dace_runkernel_map_fusion_wrapper_0_0_15(benchmark_const_assignment_fusion_test_assign_bounary_3d_state_t *__state, float * __restrict__ gpu_A, int K, int M, int N)
{

    if ((int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32)) == 0 || (int_ceil(int_ceil((Max((K - 1), (M - 1)) + 1), 1), 1)) == 0) {

        return;
    }

    void  *map_fusion_wrapper_0_0_15_args[] = { (void *)&gpu_A, (void *)&K, (void *)&M, (void *)&N };
    gpuError_t __err = cudaLaunchKernel((void*)map_fusion_wrapper_0_0_15, dim3(int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32), int_ceil(int_ceil((Max((K - 1), (M - 1)) + 1), 1), 1), 1), dim3(32, 1, 1), map_fusion_wrapper_0_0_15_args, 0, __state->gpu_context->streams[0]);
    DACE_KERNEL_LAUNCH_CHECK(__err, "map_fusion_wrapper_0_0_15", int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32), int_ceil(int_ceil((Max((K - 1), (M - 1)) + 1), 1), 1), 1, 32, 1, 1);
}

