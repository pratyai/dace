[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected

tests/transformations/benchmark_const_assignment_fusion_test.py 
Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.8527314823586494 ms
2D boundary init: original op
Instrumentation report
SDFG Hash: 75870eb1172f328e22b1918bf0ef0eaea2d8d72e5ad88f27dc302548348e6a40
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.828          1.854          1.853          1.912          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.8585919751785696 ms
2D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: c84cc8ef2bd5a7660e27e5418057ac03ef24dc6be628ff60c1b57c5a25b1885c
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.840          1.861          1.859          2.041          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 1.8556269933469594 ms
2D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: c1df81826a78edd515d588730b7e307937287cb11b79ff095bee40906cbc61b7
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              1.833          1.858          1.856          1.892          
---------------------------------------------------------------------------

[32m.[0m
Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 53.868898015934974 ms
3D boundary init: original op
Instrumentation report
SDFG Hash: 635fe35c5dd65bba081e5f2d955aaf90ae695e05ded70070e3ad20706feda1a1
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              53.717         53.896         53.869         55.175         
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 55.07206346374005 ms
3D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: 4bf6d7b82a9ebfdb508d3d0c3b7576da94221ed7430a3fed6f51cfcd929bedf9
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              54.965         55.077         55.072         55.487         
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 55.40322500746697 ms
3D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: 60bfe62035e5a945210116c4671f12406963f578ed61e0b60106407f94f4648f
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              55.198         55.404         55.403         55.610         
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
[33m=========== [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m15 warnings[0m[33m in 180.02s (0:03:00)[0m[33m ===========[0m
