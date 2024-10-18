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
