
#include <cuda_runtime.h>
#include <dace/dace.h>


struct benchmark_const_assignment_fusion_test_assign_top_row_state_t {
    dace::cuda::Context *gpu_context;
};



DACE_EXPORTED int __dace_init_cuda(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, int M, int N);
DACE_EXPORTED int __dace_exit_cuda(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state);



int __dace_init_cuda(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, int M, int N) {
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

    

    __state->gpu_context = new dace::cuda::Context(1, 1);

    // Create cuda streams and events
    for(int i = 0; i < 1; ++i) {
        DACE_GPU_CHECK(cudaStreamCreateWithFlags(&__state->gpu_context->internal_streams[i], cudaStreamNonBlocking));
        __state->gpu_context->streams[i] = __state->gpu_context->internal_streams[i]; // Allow for externals to modify streams
    }
    for(int i = 0; i < 1; ++i) {
        DACE_GPU_CHECK(cudaEventCreateWithFlags(&__state->gpu_context->events[i], cudaEventDisableTiming));
    }

    

    return 0;
}

int __dace_exit_cuda(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state) {
    

    // Synchronize and check for CUDA errors
    int __err = static_cast<int>(__state->gpu_context->lasterror);
    if (__err == 0)
        __err = static_cast<int>(cudaDeviceSynchronize());

    // Destroy cuda streams and events
    for(int i = 0; i < 1; ++i) {
        DACE_GPU_CHECK(cudaStreamDestroy(__state->gpu_context->internal_streams[i]));
    }
    for(int i = 0; i < 1; ++i) {
        DACE_GPU_CHECK(cudaEventDestroy(__state->gpu_context->events[i]));
    }

    delete __state->gpu_context;
    return __err;
}

DACE_EXPORTED bool __dace_gpu_set_stream(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, int streamid, gpuStream_t stream)
{
    if (streamid < 0 || streamid >= 1)
        return false;

    __state->gpu_context->streams[streamid] = stream;

    return true;
}

DACE_EXPORTED void __dace_gpu_set_all_streams(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, gpuStream_t stream)
{
    for (int i = 0; i < 1; ++i)
        __state->gpu_context->streams[i] = stream;
}

__global__ void __launch_bounds__(32) map_fusion_wrapper_0_0_9(float * __restrict__ gpu_A, int M, int N) {
    {
        int t = (blockIdx.x * 32 + threadIdx.x);
        if (t < (Max((M - 1), (N - 1)) + 1)) {
            {
                for (auto gsl_t = t; gsl_t < N; gsl_t += N) {
                    {
                        float __out;

                        ///////////////////
                        // Tasklet code (assign_19_8)
                        __out = 1;
                        ///////////////////

                        gpu_A[t] = __out;
                    }
                    {
                        float __out;

                        ///////////////////
                        // Tasklet code (assign_25_8)
                        __out = 1;
                        ///////////////////

                        gpu_A[(t + (N * (M - 1)))] = __out;
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

                        gpu_A[(t * N)] = __out;
                    }
                    {
                        float __out;

                        ///////////////////
                        // Tasklet code (assign_37_8)
                        __out = 1;
                        ///////////////////

                        gpu_A[(((t * N) + N) - 1)] = __out;
                    }
                }
            }
        }
    }
}


DACE_EXPORTED void __dace_runkernel_map_fusion_wrapper_0_0_9(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, float * __restrict__ gpu_A, int M, int N);
void __dace_runkernel_map_fusion_wrapper_0_0_9(benchmark_const_assignment_fusion_test_assign_top_row_state_t *__state, float * __restrict__ gpu_A, int M, int N)
{

    if ((int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32)) == 0) {

        return;
    }

    void  *map_fusion_wrapper_0_0_9_args[] = { (void *)&gpu_A, (void *)&M, (void *)&N };
    gpuError_t __err = cudaLaunchKernel((void*)map_fusion_wrapper_0_0_9, dim3(int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32), 1, 1), dim3(32, 1, 1), map_fusion_wrapper_0_0_9_args, 0, __state->gpu_context->streams[0]);
    DACE_KERNEL_LAUNCH_CHECK(__err, "map_fusion_wrapper_0_0_9", int_ceil(int_ceil((Max((M - 1), (N - 1)) + 1), 1), 32), 1, 1, 32, 1, 1);
}

