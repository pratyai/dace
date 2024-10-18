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
|-State (0)                                                                
| |-Node (0, Map _numpy_full__map)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          9.699          9.918          9.739          10.679         
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (36, Map _Sub__map)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          18.330         18.941         18.876         22.629         
---------------------------------------------------------------------------
|-State (4)                                                                
| |-Node (86, Map assign_112_8_map)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          0.007          0.117          0.010          1.630          
---------------------------------------------------------------------------
| |-Node (89, Map outer_fused)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          70.657         84.072         83.079         109.482        
---------------------------------------------------------------------------
|-State (5)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          0.030          0.077          0.036          1.383          
---------------------------------------------------------------------------
|-State (6)                                                                
| |-Node (10, Map map_fusion_wrapper)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          0.034          0.070          0.036          1.146          
---------------------------------------------------------------------------
|-State (8)                                                                
| |-Node (38, Map _Mult__map)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          17.711         17.910         17.909         19.328         
---------------------------------------------------------------------------
|-State (9)                                                                
| |-Node (0, Map assign_82_8_map)                                                            
| | |Thread 9883349089150599077:                                                            
| | |          0.007          0.027          0.009          1.586          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/npbench/misc/cavity_flow_test.py::test_cpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m============ [32m1 passed[0m, [33m[1m3 deselected[0m, [33m[1m1 warning[0m[33m in 816.72s (0:13:36)[0m[33m ============[0m
