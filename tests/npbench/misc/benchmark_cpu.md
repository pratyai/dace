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
| | |Thread 15567262608649888491:                                                            
| | |          9.561          10.053         9.622          12.313         
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (36, Map _Sub__map)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          18.330         18.924         18.834         21.948         
---------------------------------------------------------------------------
|-State (4)                                                                
| |-Node (86, Map assign_112_8_map)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          0.007          0.114          0.011          1.117          
---------------------------------------------------------------------------
| |-Node (89, Map outer_fused)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          79.286         92.234         87.697         158.494        
---------------------------------------------------------------------------
|-State (5)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          0.030          0.081          0.037          1.123          
---------------------------------------------------------------------------
|-State (6)                                                                
| |-Node (6, Map map_fusion_wrapper)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          0.007          0.047          0.009          1.101          
---------------------------------------------------------------------------
|-State (7)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          0.032          0.065          0.034          1.635          
---------------------------------------------------------------------------
|-State (9)                                                                
| |-Node (38, Map _Mult__map)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          17.738         17.883         17.867         19.604         
---------------------------------------------------------------------------
|-State (10)                                                               
| |-Node (0, Map assign_82_8_map)                                                            
| | |Thread 15567262608649888491:                                                            
| | |          0.007          0.022          0.009          1.448          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/npbench/misc/cavity_flow_test.py::test_cpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m============ [32m1 passed[0m, [33m[1m3 deselected[0m, [33m[1m1 warning[0m[33m in 821.56s (0:13:41)[0m[33m ============[0m
