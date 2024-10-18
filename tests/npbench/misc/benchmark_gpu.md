[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 3 deselected / 1 selected

tests/npbench/misc/cavity_flow_test.py Parsing complete.
Warmup...
Actual...
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|-State (1)                                                                
| |-Node (36, Map _Sub__map)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          14.335         14.840         14.858         15.198         
---------------------------------------------------------------------------
|-State (2)                                                                
| |-Node (86, Map assign_112_8_map)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.004          0.005          0.005          0.018          
---------------------------------------------------------------------------
| |-Node (89, Map outer_fused)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          7.277          7.470          7.476          7.669          
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.004          0.004          0.004          0.016          
---------------------------------------------------------------------------
|-State (4)                                                                
| |-Node (6, Map map_fusion_wrapper)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.002          0.004          0.004          0.014          
---------------------------------------------------------------------------
|-State (5)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.004          0.005          0.004          0.018          
---------------------------------------------------------------------------
|-State (7)                                                                
| |-Node (38, Map _Mult__map)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          2.537          2.631          2.634          2.931          
---------------------------------------------------------------------------
|-State (8)                                                                
| |-Node (0, Map assign_82_8_map)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.002          0.003          0.003          0.014          
---------------------------------------------------------------------------
|-State (9)                                                                
| |-Node (6, Map _numpy_full__map)                                                            
| | |Thread 5458639261110511847:                                                            
| | |          0.478          0.479          0.479          0.481          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "_numpy_full__map". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "_Sub__map". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "_Mult__map". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "assign_82_8_map". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "outer_fused". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "assign_112_8_map". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

tests/npbench/misc/cavity_flow_test.py::test_gpu
  /home/pmazumder/gitspace/dace/dace/codegen/targets/cuda.py:1869: UserWarning: No `gpu_block_size` property specified on map "map_fusion_wrapper". Falling back to the configuration entry `compiler.cuda.default_block_size`: 32,1,1. You can either specify the block size to use with the gpu_block_size property, or by adding nested `GPU_ThreadBlock` maps, which map work to individual threads. For more information, see https://spcldace.readthedocs.io/en/latest/optimization/gpu.html
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m=========== [32m1 passed[0m, [33m[1m3 deselected[0m, [33m[1m8 warnings[0m[33m in 162.22s (0:02:42)[0m[33m ============[0m
