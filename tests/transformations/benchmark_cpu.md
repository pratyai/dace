[1m============================= test session starts ==============================[0m
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/pmazumder/gitspace/dace
configfile: pytest.ini
collected 4 items / 2 deselected / 2 selected

tests/transformations/benchmark_const_assignment_fusion_test.py 
Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 0.019409984815865755 ms
2D boundary init: original op
Instrumentation report
SDFG Hash: db6fa90ab8d685b446338efc5ad760e48a07014cbf6278414ca5b9c6f2226f6e
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.018          0.020          0.019          0.146          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 0.011969998013228178 ms
2D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: edb0867e1b184f47b8dd85607393c78a6a1e28014ce8b89d2b470a12d26ab655
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.011          0.012          0.012          0.030          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_top_row 0.007860013283789158 ms
2D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: 96e1a5d4636e5ad24a429bc5a5714f146fd3850b97ad13a919600b5263772ddb
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.007          0.008          0.008          0.038          
---------------------------------------------------------------------------

[32m.[0m
Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.12180002522654831 ms
3D boundary init: original op
Instrumentation report
SDFG Hash: bb26da97fcc245ebb747a0f69b8dce6e2fbd4386eda60301fdba7582af437e92
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.117          0.124          0.122          0.447          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.0994600122794509 ms
3D boundary init: fused op w/o. grid-strided loop
Instrumentation report
SDFG Hash: 271f9609dd2a193844b2ea6cb8f59f0bd51b9744f1689b31daeda0d47148ba0c
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.094          0.101          0.099          0.325          
---------------------------------------------------------------------------


Profiling...
benchmark_const_assignment_fusion_test_assign_bounary_3d 0.09554999996908009 ms
3D boundary init: fused op with grid-strided loop
Instrumentation report
SDFG Hash: db58f0183dcec3550a9c8a4bab8596afcc0dbe348f55d31d444a0dc9e9338305
---------------------------------------------------------------------------
Element        Runtime (ms)   
               Min            Mean           Median         Max            
---------------------------------------------------------------------------
SDFG (0)                                                                   
|:                                                                         
|              0.093          0.096          0.096          0.112          
---------------------------------------------------------------------------

[32m.[0m

[33m=============================== warnings summary ===============================[0m
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
  /home/pmazumder/gitspace/dace/venv/lib/python3.12/site-packages/astunparse/unparser.py:711: DeprecationWarning: ast.Num is deprecated and will be removed in Python 3.14; use ast.Constant instead
    if isinstance(t.value, getattr(ast, 'Constant', getattr(ast, 'Num', None))) and isinstance(t.value.n, int):

tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_2d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_cpu
tests/transformations/benchmark_const_assignment_fusion_test.py::test_benchmark_3d_boundary_init_cpu
  /home/pmazumder/gitspace/dace/dace/frontend/operations.py:75: UserWarning: Cannot show profiling progress, missing optional dependency tqdm...
  	To see a live progress bar please install tqdm (`pip install tqdm`)
  	To disable this feature (and this warning) set `profiling_status` to false in the dace config (~/.dace.conf).
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[33m================= [32m2 passed[0m, [33m[1m2 deselected[0m, [33m[1m7 warnings[0m[33m in 24.09s[0m[33m =================[0m
