#!/bin/bash

python -m pytest tests/npbench/misc/cavity_flow_test.py -k gpu -s 2>&1 > tests/npbench/misc/benchmark_gpu.md
sed -i 's/.*Profiling: .*//' tests/npbench/misc/benchmark_gpu.md
rm -rf tests/npbench/misc/_gpugraphs
mv _dacegraphs tests/npbench/misc/_gpugraphs

python -m pytest tests/npbench/misc/cavity_flow_test.py -k cpu -s 2>&1 > tests/npbench/misc/benchmark_cpu.md
sed -i 's/.*Profiling: .*//' tests/npbench/misc/benchmark_cpu.md
rm -rf tests/npbench/misc/_cpugraphs
mv _dacegraphs tests/npbench/misc/_cpugraphs

mv *DeviceType*.json tests/npbench/misc/



SUFFIX="w_CMF_w_gsl"

rm -rf "tests/npbench/misc/_cpugraphs_${SUFFIX}"
mv tests/npbench/misc/_cpugraphs "tests/npbench/misc/_cpugraphs_${SUFFIX}"
rm -rf "tests/npbench/misc/_gpugraphs_${SUFFIX}"
mv tests/npbench/misc/_gpugraphs "tests/npbench/misc/_gpugraphs_${SUFFIX}"
mv tests/npbench/misc/benchmark_cpu.md "tests/npbench/misc/benchmark_cpu_${SUFFIX}.text"
mv tests/npbench/misc/benchmark_gpu.md "tests/npbench/misc/benchmark_gpu_${SUFFIX}.text"

mv tests/npbench/misc/pre_DeviceType.CPU.json "tests/npbench/misc/pre_DeviceType.CPU_${SUFFIX}.json"
mv tests/npbench/misc/pre_DeviceType.GPU.json "tests/npbench/misc/pre_DeviceType.GPU_${SUFFIX}.json"
mv tests/npbench/misc/post_DeviceType.CPU.json "tests/npbench/misc/post_DeviceType.CPU_${SUFFIX}.json"
mv tests/npbench/misc/post_DeviceType.GPU.json "tests/npbench/misc/post_DeviceType.GPU_${SUFFIX}.json"
