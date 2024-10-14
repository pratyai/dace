import os
from copy import deepcopy

import numpy as np

import dace
from dace import SDFG, DeviceType
from dace.transformation.auto import auto_optimize
from dace.transformation.dataflow.const_assignment_fusion import ConstAssignmentStateFusion

K = dace.symbol('K')
M = dace.symbol('M')
N = dace.symbol('N')


@dace.program
def assign_top_row(A: dace.float32[M, N]):
    for t in dace.map[0:N]:
        A[0, t] = 1


@dace.program
def assign_bottom_row(A: dace.float32[M, N]):
    for b in dace.map[0:N]:
        A[M - 1, b] = 1


@dace.program
def assign_left_col(A: dace.float32[M, N]):
    for l in dace.map[0:M]:
        A[l, 0] = 1


@dace.program
def assign_right_col(A: dace.float32[M, N]):
    for r in dace.map[0:M]:
        A[r, N - 1] = 1


def assign_bounary_sdfg():
    st0 = assign_top_row.to_sdfg(simplify=True, validate=True, use_cache=False)
    st0.start_block.label = 'st0'

    st1 = assign_bottom_row.to_sdfg(simplify=True, validate=True, use_cache=False)
    st1.start_block.label = 'st1'
    st0.add_edge(st0.start_state, st1.start_state, dace.InterstateEdge())

    st2 = assign_left_col.to_sdfg(simplify=True, validate=True, use_cache=False)
    st2.start_block.label = 'st2'
    st0.add_edge(st1.start_state, st2.start_state, dace.InterstateEdge())

    st3 = assign_right_col.to_sdfg(simplify=True, validate=True, use_cache=False)
    st3.start_block.label = 'st3'
    st0.add_edge(st2.start_state, st3.start_state, dace.InterstateEdge())

    return st0


@dace.program
def assign_top_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:M, 0:N]:
        A[0, t1, t2] = 1


@dace.program
def assign_bottom_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:M, 0:N]:
        A[K - 1, t1, t2] = 1


@dace.program
def assign_front_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:K, 0:N]:
        A[t1, 0, t2] = 1


@dace.program
def assign_back_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:K, 0:N]:
        A[t1, M - 1, t2] = 1


@dace.program
def assign_left_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:K, 0:M]:
        A[t1, t2, 0] = 1


@dace.program
def assign_right_face(A: dace.float32[K, M, N]):
    for t1, t2 in dace.map[0:K, 0:M]:
        A[t1, t2, N - 1] = 1


@dace.program
def assign_bounary_3d(A: dace.float32[K, M, N]):
    assign_top_face(A)
    assign_bottom_face(A)
    assign_front_face(A)
    assign_back_face(A)
    assign_left_face(A)
    assign_right_face(A)


def benchmark_2d_boundary_init(device: DeviceType = DeviceType.CPU):
    m, n = 1000, 2000
    A = np.random.uniform(size=(m, n)).astype(np.float32)

    def original_op():
        g = assign_bounary_sdfg()  # Construct SDFG with the maps on separate states.
        auto_optimize.set_fast_implementations(g, device)
        g.simplify()
        # g = auto_optimize.auto_optimize(g, device)
        g.validate()
        g.compile()
        return g

    def fused_op(use_grid_strided_loops: bool):
        g = assign_bounary_sdfg()  # Construct SDFG with the maps on separate states.
        g.apply_transformations_repeated(ConstAssignmentStateFusion,
                                         options={'use_grid_strided_loops': use_grid_strided_loops})
        auto_optimize.set_fast_implementations(g, device)
        g.simplify()
        # g = auto_optimize.auto_optimize(g, device)
        g.validate()
        g.compile()
        return g

    # === Part 1: Original Op === #
    g = deepcopy(original_op())
    g.save(os.path.join('_dacegraphs', 'big-0.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    actual_A = deepcopy(A)
    with dace.profile(repetitions=1000, warmup=10) as prof:
        g(A=actual_A, M=m, N=n)
    print(prof.report)

    # === Part 2: Fused Op w/o. grid-strided loop === #
    g = deepcopy(fused_op(False))
    g.save(os.path.join('_dacegraphs', 'big-1.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    our_A = deepcopy(A)
    with dace.profile(repetitions=1000, warmup=10) as prof:
        g(A=our_A, M=m, N=n)
    print(prof.report)
    assert np.all(np.equal(our_A, actual_A))

    # === Part 3: Fused Op w. grid-strided loop === #
    g = deepcopy(fused_op(True))
    g.save(os.path.join('_dacegraphs', 'big-2.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    our_A = deepcopy(A)
    with dace.profile(repetitions=1000, warmup=10) as prof:
        g(A=our_A, M=m, N=n)
    print(prof.report)
    assert np.all(np.equal(our_A, actual_A))


def benchmark_3d_boundary_init(device: DeviceType = DeviceType.CPU):
    k, m, n = 300, 400, 500
    A = np.random.uniform(size=(k, m, n)).astype(np.float32)

    def original_op():
        g = assign_bounary_3d.to_sdfg(simplify=True, validate=True, use_cache=False)
        auto_optimize.set_fast_implementations(g, device)
        g.simplify()
        # g = auto_optimize.auto_optimize(g, device)
        g.validate()
        g.compile()
        return g

    def fused_op(use_grid_strided_loops: bool):
        g = assign_bounary_3d.to_sdfg(simplify=True, validate=True, use_cache=False)
        g.apply_transformations_repeated(ConstAssignmentStateFusion,
                                         options={'use_grid_strided_loops': use_grid_strided_loops})
        auto_optimize.set_fast_implementations(g, device)
        g.simplify()
        # g = auto_optimize.auto_optimize(g, device)
        g.validate()
        g.compile()
        return g

    # === Part 1: Original Op === #
    g = deepcopy(original_op())
    g.save(os.path.join('_dacegraphs', '3d-big-0.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    actual_A = deepcopy(A)
    with dace.profile(repetitions=1000, warmup=10) as prof:
        g(A=actual_A, K=k, M=m, N=n)
    print(prof.report)

    # === Part 2: Fused Op w/o. grid-strided loop === #
    g = deepcopy(fused_op(False))
    g.save(os.path.join('_dacegraphs', '3d-big-1.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    our_A = deepcopy(A)
    with dace.profile(repetitions=1000, warmup=10) as prof:
        g(A=our_A, K=k, M=m, N=n)
    print(prof.report)
    assert np.all(np.equal(our_A, actual_A))

    # === Part 3: Fused Op w. grid-strided loop === #
    g = deepcopy(fused_op(True))
    g.save(os.path.join('_dacegraphs', '3d-big-2.sdfg'))
    # g.instrument = dace.InstrumentationType.Timer
    our_A = deepcopy(A)
    with dace.profile(repetitions=100, warmup=10) as prof:
        g(A=our_A, K=k, M=m, N=n)
    print(prof.report)
    assert np.all(np.equal(our_A, actual_A))


def test_benchmark_2d_boundary_init_cpu():
    benchmark_2d_boundary_init(DeviceType.CPU)


def test_benchmark_2d_boundary_init_gpu():
    benchmark_2d_boundary_init(DeviceType.GPU)


def test_benchmark_3d_boundary_init_cpu():
    benchmark_3d_boundary_init(DeviceType.CPU)


def test_benchmark_3d_boundary_init_gpu():
    benchmark_3d_boundary_init(DeviceType.GPU)


if __name__ == '__main__':
    test_benchmark_2d_boundary_init_cpu()
    test_benchmark_2d_boundary_init_gpu()
    test_benchmark_3d_boundary_init_cpu()
    test_benchmark_3d_boundary_init_gpu()
