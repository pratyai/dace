[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected

tests/transformations/benchmark_const_assignment_fusion_test.py 
Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.6687044990248978 ms
2D boundary init: original op
Instrumentation report
SDFG Hash: deedd03b7967cf173b4cb271321a927bc07db31856f54ceb1f3a343cb709df5b
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.660          1.672          1.669          1.706          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.7102595011238009 ms
2D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: 2f0f2fdf3e358e767ac1a9905067a1b1e42f2e8df6c0752f91ed6564dd2f83b1
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.696          1.712          1.710          2.045          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.6706089954823256 ms
2D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: 61fa63062f25b965f156c47bbf1def31b6768032145ee2d2cdafa4c63dc480b5
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.654          1.672          1.671          2.091          
---------------------------------------------------------------------------

[32m.[0m
Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 48.091168981045485 ms
3D boundary init: original op
Instrumentation report
SDFG Hash: 00cc99207ab813359ca287b6ffc0f526e61ef58d103565ae2fbff317eb6ff6a0
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              47.897         48.108         48.091         52.113         
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 48.694633529521525 ms
3D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: b63a48b3d50a88f93126fe791fd76260e82a7b6e43bbb1fac21589e536a75ba8
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              48.561         48.717         48.695         49.539         
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 49.010923015885055 ms
3D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: d042faecc18627c7716692bf69b0b13dfbbbbb5a2b928830656d1f869bfa77b9
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              48.888         49.019         49.011         49.294         
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_top_row_18". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_bottom_row_24". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_left_col_30". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_right_col_36". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/frontend/operations.py:75: UserWarning: Cannot show profiling progress, missing optional dependency tqdm...
  	To see a live progress bar please install tqdm (`pip install tqdm`)
  	To disable this feature (and this warning) set `profiling_status` to false in the dace config (~/.dace.conf).
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "map_fusion_wrapper". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_top_face_61". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_bottom_face_67". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_front_face_73". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_back_face_79". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_left_face_85". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_right_face_91". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m=========== [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m15 warnings[0m[33m in 171.58s (0:02:51)[0m[33m ===========[0m
