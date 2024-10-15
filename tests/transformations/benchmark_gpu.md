[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected


benchmark_const_assignment_fusion_test_assign_top_row_0 167.06380699179135 ms
===2D boundary init: original op===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              166.200        167.907        167.064        172.466        
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_top_row_47)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.002          0.004          0.004          0.009          
---------------------------------------------------------------------------
|-State (1)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_bottom_row_53)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.004          0.005          0.004          0.018          
---------------------------------------------------------------------------
|-State (2)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_left_col_59)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.004          0.006          0.006          0.014          
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_right_col_65)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.005          0.006          0.006          0.014          
---------------------------------------------------------------------------


benchmark_const_assignment_fusion_test_assign_top_row_0 170.15381151577458 ms
===2D boundary init: fused op w/o. grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              166.765        169.892        170.154        172.003        
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (6, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.003          0.004          0.004          0.008          
---------------------------------------------------------------------------
| |-Node (11, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.008          0.009          0.008          0.022          
---------------------------------------------------------------------------


benchmark_const_assignment_fusion_test_assign_top_row_0 165.11968348640949 ms
===2D boundary init: fused op with grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              164.683        165.159        165.120        167.484        
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (10, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.007          0.008          0.008          0.013          
---------------------------------------------------------------------------


benchmark_const_assignment_fusion_test_assign_bounary_3d 50.67180350306444 ms
===3D boundary init: original op===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              49.457         50.629         50.672         51.666         
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_top_face_90)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.008          0.008          0.008          0.013          
---------------------------------------------------------------------------
|-State (1)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_bottom_face_9)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.008          0.009          0.010          0.023          
---------------------------------------------------------------------------
|-State (2)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_front_face_10)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.008          0.008          0.008          0.024          
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_back_face_108)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.006          0.008          0.008          0.027          
---------------------------------------------------------------------------
|-State (4)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_left_face_114)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.042          0.044          0.044          0.053          
---------------------------------------------------------------------------
|-State (5)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_right_face_12)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.044          0.045          0.045          0.055          
---------------------------------------------------------------------------


benchmark_const_assignment_fusion_test_assign_bounary_3d 50.77531602000818 ms
===3D boundary init: fused op w/o. grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              50.484         50.773         50.775         51.235         
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (6, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.008          0.008          0.008          0.012          
---------------------------------------------------------------------------
| |-Node (11, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.006          0.008          0.008          0.020          
---------------------------------------------------------------------------
| |-Node (16, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.050          0.052          0.052          0.065          
---------------------------------------------------------------------------


benchmark_const_assignment_fusion_test_assign_bounary_3d 49.49491852312349 ms
===3D boundary init: fused op with grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              49.321         49.533         49.495         50.064         
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (16, Map map_fusion_wrapper)                                                            
| | |Thread 3118465057716905996:                                                            
| | |          0.055          0.057          0.057          0.063          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_top_row_47". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_bottom_row_53". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_left_col_59". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_right_col_65". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/sdfg/sdfg.py:2291: UserWarning: SDFG "benchmark_const_assignment_fusion_test_assign_top_row" is already loaded by another object, recompiling under a different name.
    warnings.warn('SDFG "%s" is already loaded by another object, '

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/transformation/dataflow/redundant_array.py:289: UserWarning: validate_subsets failed: Neither source nor destination subsets are defined
    warnings.warn(f'validate_subsets failed: {ex}')

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_gpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "map_fusion_wrapper". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_top_face_90". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_bottom_face_96". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_front_face_102". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_back_face_108". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_left_face_114". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "benchmark_const_assignment_fusion_test_assign_right_face_120". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m=========== [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m16 warnings[0m[33m in 734.67s (0:12:14)[0m[33m ===========[0m
