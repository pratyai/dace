[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected

tests/transformations/benchmark_const_assignment_fusion_test.py Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  77%|███████▋  | 775/1010 [00:00<00:00, 7744.15it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 7753.14it/s]
benchmark_const_assignment_fusion_test_assign_top_row_0 0.13079101336188614 ms
===2D boundary init: original op===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.108          0.128          0.131          0.366          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_top_row_47)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.007          0.020          0.021          0.045          
---------------------------------------------------------------------------
|-State (1)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_bottom_row_53)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.005          0.006          0.006          0.010          
---------------------------------------------------------------------------
|-State (2)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_left_col_59)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.004          0.005          0.005          0.024          
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_right_col_65)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.004          0.006          0.005          0.100          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  89%|████████▉ | 900/1010 [00:00<00:00, 8996.62it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 8984.27it/s]
benchmark_const_assignment_fusion_test_assign_top_row_0 0.11151551734656096 ms
===2D boundary init: fused op w/o. grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.090          0.111          0.112          0.920          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.014          0.021          0.018          0.151          
---------------------------------------------------------------------------
| |-Node (9, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.004          0.006          0.005          0.054          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  96%|█████████▌| 972/1010 [00:00<00:00, 9715.45it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 9689.16it/s]
benchmark_const_assignment_fusion_test_assign_top_row_0 0.10572001338005066 ms
===2D boundary init: fused op with grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.084          0.103          0.106          0.393          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (8, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.009          0.022          0.022          0.024          
---------------------------------------------------------------------------

[32m.[0mProfiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  42%|████▏     | 425/1010 [00:00<00:00, 4246.75it/s]Profiling:  85%|████████▍ | 855/1010 [00:00<00:00, 4273.45it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 4271.55it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.23336600861512125 ms
===3D boundary init: original op===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.214          0.233          0.233          0.497          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_top_face_90)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.020          0.027          0.027          0.054          
---------------------------------------------------------------------------
|-State (1)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_bottom_face_9)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.013          0.015          0.014          0.038          
---------------------------------------------------------------------------
|-State (2)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_front_face_10)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.012          0.013          0.013          0.035          
---------------------------------------------------------------------------
|-State (3)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_back_face_108)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.010          0.011          0.011          0.038          
---------------------------------------------------------------------------
|-State (4)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_left_face_114)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.029          0.031          0.031          0.051          
---------------------------------------------------------------------------
|-State (5)                                                                
| |-Node (0, Map benchmark_const_assignment_fusion_test_assign_right_face_12)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.024          0.026          0.025          0.051          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  51%|█████▏    | 519/1010 [00:00<00:00, 5187.11it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 5194.85it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.19121551304124296 ms
===3D boundary init: fused op w/o. grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.173          0.192          0.191          0.427          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (4, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.026          0.033          0.033          0.056          
---------------------------------------------------------------------------
| |-Node (9, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.018          0.020          0.020          0.082          
---------------------------------------------------------------------------
| |-Node (14, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.037          0.043          0.042          0.066          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  53%|█████▎    | 531/1010 [00:00<00:00, 5304.71it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 5295.55it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.18826551968231797 ms
===3D boundary init: fused op with grid-strided loop===
Instrumentation report
SDFG Hash: 
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.170          0.188          0.188          0.469          
---------------------------------------------------------------------------
|-State (0)                                                                
| |-Node (14, Map map_fusion_wrapper)                                                            
| | |Thread 12176263715017013721:                                                            
| | |          0.091          0.099          0.096          0.200          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
  /home/pmazumder/gitspace/dace/dace/sdfg/sdfg.py:2291: UserWarning: SDFG "benchmark_const_assignment_fusion_test_assign_top_row" is already loaded by another object, recompiling under a different name.
    warnings.warn('SDFG "%s" is already loaded by another object, '

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m================= [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m4 warnings[0m[33m in 30.11s[0m[33m =================[0m
