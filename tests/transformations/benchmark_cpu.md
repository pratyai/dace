[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected

tests/transformations/benchmark_const_assignment_fusion_test.py Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 49408.06it/s]
benchmark_const_assignment_fusion_test_assign_top_row 0.019659986719489098 ms
2D boundary init: original op
Instrumentation report
SDFG Hash: db6fa90ab8d685b446338efc5ad760e48a07014cbf6278414ca5b9c6f2226f6e
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.018          0.020          0.020          0.037          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 80106.03it/s]
benchmark_const_assignment_fusion_test_assign_top_row 0.012320000678300858 ms
2D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: edb0867e1b184f47b8dd85607393c78a6a1e28014ce8b89d2b470a12d26ab655
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.011          0.012          0.012          0.025          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 118053.92it/s]
benchmark_const_assignment_fusion_test_assign_top_row 0.00832002842798829 ms
2D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: 96e1a5d4636e5ad24a429bc5a5714f146fd3850b97ad13a919600b5263772ddb
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.007          0.008          0.008          0.025          
---------------------------------------------------------------------------

[32m.[0mProfiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling:  88%|████████▊ | 892/1010 [00:00<00:00, 8908.90it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 8891.42it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.11037098011001945 ms
3D boundary init: original op
Instrumentation report
SDFG Hash: bb26da97fcc245ebb747a0f69b8dce6e2fbd4386eda60301fdba7582af437e92
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.109          0.112          0.110          0.358          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/1010 [00:00<?, ?it/s]Profiling: 100%|██████████| 1010/1010 [00:00<00:00, 11487.75it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.08548051118850708 ms
3D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: 271f9609dd2a193844b2ea6cb8f59f0bd51b9744f1689b31daeda0d47148ba0c
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.083          0.086          0.085          0.155          
---------------------------------------------------------------------------

Profiling:   0%|          | 0/110 [00:00<?, ?it/s]Profiling: 100%|██████████| 110/110 [00:00<00:00, 10045.58it/s]
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.0935050193220377 ms
3D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: db58f0183dcec3550a9c8a4bab8596afcc0dbe348f55d31d444a0dc9e9338305
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.092          0.094          0.094          0.108          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m================= [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m1 warning[0m[33m in 23.27s[0m[33m ==================[0m
