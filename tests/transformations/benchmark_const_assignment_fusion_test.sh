#!/bin/bash

python -m pytest tests/transformations/benchmark_const_assignment_fusion_test.py -k cpu -s 2>&1 > tests/transformations/benchmark_cpu.md
sed -i 's/.*Profiling: .*//' tests/transformations/benchmark_cpu.md
rm -rf tests/transformations/_cpugraphs
mv _dacegraphs tests/transformations/_cpugraphs
python -m pytest tests/transformations/benchmark_const_assignment_fusion_test.py -k gpu -s 2>&1 > tests/transformations/benchmark_gpu.md
sed -i 's/.*Profiling: .*//' tests/transformations/benchmark_gpu.md
rm -rf tests/transformations/_gpugraphs
mv _dacegraphs tests/transformations/_gpugraphs
