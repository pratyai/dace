# Copyright 2019-2022 ETH Zurich and the DaCe authors. All rights reserved.
# Original application code: NPBench - https://github.com/spcl/npbench
import os
from copy import deepcopy

import dace.dtypes
import numpy as np
import dace
import pytest
import argparse
from dace import SDFG
from dace.sdfg.nodes import MapEntry
from dace import DeviceType, SDFG, GPU_SCHEDULES, InstrumentationType, CPU_SCHEDULES
from dace.transformation.auto.auto_optimize import auto_optimize, fpga_auto_opt
from dace.fpga_testing import fpga_test
from dace.transformation.interstate import FPGATransformSDFG, InlineSDFG
from dace.codegen.instrumentation import InstrumentationReport
from dace.transformation.dataflow.const_assignment_fusion import ConstAssignmentStateFusion

from typing import Optional
import tqdm

nx, ny, nit = (dace.symbol(s, dace.int64) for s in ('nx', 'ny', 'nit'))


def instrument_map_kernels(g: SDFG):
    for n, st in g.all_nodes_recursive():
        if not isinstance(n, MapEntry):
            continue
        if n.map.schedule in CPU_SCHEDULES:
            n.map.instrument = InstrumentationType.Timer
            # st.instrument = InstrumentationType.Timer
        elif n.map.schedule in GPU_SCHEDULES:
            n.map.instrument = InstrumentationType.GPU_Events
            # st.instrument = InstrumentationType.GPU_Events
    # g.instrument = InstrumentationType.Timer
    g.clear_instrumentation_reports()


def produce_combined_instrumentation_report(g: SDFG, filename: Optional[str] = None) -> Optional[InstrumentationReport]:
    all_ins = g.get_instrumentation_reports()
    if not all_ins:
        return None
    ins = InstrumentationReport(filename='')
    for i in all_ins:
        ins.events.extend(deepcopy(i.events))
    ins.process_events()
    if filename:
        ins.save(filename)
    return ins


def relerror(val, ref):
    if np.linalg.norm(ref) == 0:
        return np.linalg.norm(val - ref)
    return np.linalg.norm(val - ref) / np.linalg.norm(ref)


@dace.program
def build_up_b(b: dace.float64[ny, nx], rho: dace.float64, dt: dace.float64, u: dace.float64[ny, nx],
               v: dace.float64[ny, nx], dx: dace.float64, dy: dace.float64):

    b[1:-1, 1:-1] = (rho * (1 / dt * ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) + (v[2:, 1:-1] - v[0:-2, 1:-1]) /
                                      (2 * dy)) - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 - 2 *
                            ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) * (v[1:-1, 2:] - v[1:-1, 0:-2]) /
                             (2 * dx)) - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))


@dace.program
def pressure_poisson(p: dace.float64[ny, nx], dx: dace.float64, dy: dace.float64, b: dace.float64[ny, nx]):
    pn = np.empty_like(p)
    pn[:] = p.copy()

    for q in range(nit):
        pn[:] = p.copy()
        p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                         (2 * (dx**2 + dy**2)) - dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

        p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 at y = 0
        p[:, 0] = p[:, 1]  # dp/dx = 0 at x = 0
        p[-1, :] = 0  # p = 0 at y = 2


@dace.program
def dace_cavity_flow(nt: dace.int64, nit: dace.int64, u: dace.float64[ny, nx], v: dace.float64[ny,
                                                                                               nx], dt: dace.float64,
                     dx: dace.float64, dy: dace.float64, p: dace.float64[ny, nx], rho: dace.float64, nu: dace.float64):
    un = np.empty_like(u)
    vn = np.empty_like(v)
    b = np.zeros((ny, nx))

    for n in range(nt):
        un[:] = u.copy()
        vn[:] = v.copy()

        build_up_b(b, rho, dt, u, v, dx, dy)
        pressure_poisson(p, dx, dy, b, nit=nit)

        u[1:-1, 1:-1] = (un[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) - dt / (2 * rho * dx) *
                         (p[1:-1, 2:] - p[1:-1, 0:-2]) + nu *
                         (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) + dt / dy**2 *
                          (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) - dt / (2 * rho * dy) *
                         (p[2:, 1:-1] - p[0:-2, 1:-1]) + nu *
                         (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) + dt / dy**2 *
                          (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

        u[0, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        u[-1, :] = 1  # set velocity on cavity lid equal to 1
        v[0, :] = 0
        v[-1, :] = 0
        v[:, 0] = 0
        v[:, -1] = 0


def numpy_cavity_flow(nx, ny, nt, nit, u, v, dt, dx, dy, p, rho, nu):

    def build_up_b(b, rho, dt, u, v, dx, dy):
        b[1:-1, 1:-1] = (rho * (1 / dt * ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) + (v[2:, 1:-1] - v[0:-2, 1:-1]) /
                                          (2 * dy)) - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 - 2 *
                                ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) * (v[1:-1, 2:] - v[1:-1, 0:-2]) /
                                 (2 * dx)) - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))

    def pressure_poisson(nit, p, dx, dy, b):
        pn = np.empty_like(p)
        pn = p.copy()

        for q in range(nit):
            pn = p.copy()
            p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                             (2 * (dx**2 + dy**2)) - dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

            p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
            p[0, :] = p[1, :]  # dp/dy = 0 at y = 0
            p[:, 0] = p[:, 1]  # dp/dx = 0 at x = 0
            p[-1, :] = 0  # p = 0 at y = 2

    un = np.empty_like(u)
    vn = np.empty_like(v)
    b = np.zeros((ny, nx))

    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        build_up_b(b, rho, dt, u, v, dx, dy)
        pressure_poisson(nit, p, dx, dy, b)

        u[1:-1, 1:-1] = (un[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) - dt / (2 * rho * dx) *
                         (p[1:-1, 2:] - p[1:-1, 0:-2]) + nu *
                         (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) + dt / dy**2 *
                          (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) - dt / (2 * rho * dy) *
                         (p[2:, 1:-1] - p[0:-2, 1:-1]) + nu *
                         (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) + dt / dy**2 *
                          (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

        u[0, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        u[-1, :] = 1  # set velocity on cavity lid equal to 1
        v[0, :] = 0
        v[-1, :] = 0
        v[:, 0] = 0
        v[:, -1] = 0


def initialize(ny, nx):
    u = np.zeros((ny, nx), dtype=np.float64)
    v = np.zeros((ny, nx), dtype=np.float64)
    p = np.zeros((ny, nx), dtype=np.float64)
    dx = 2 / (nx - 1)
    dy = 2 / (ny - 1)
    dt = .1 / ((nx - 1) * (ny - 1))
    return u, v, p, dx, dy, dt


def run_cavity_flow(device_type: dace.dtypes.DeviceType):
    '''
    Runs cavity-flow for the given device
    :return: the SDFG
    '''

    # Initialize data (npbench S size)
    # ny, nx, nt, nit, rho, nu = (61, 61, 25, 5, 1.0, 0.1)
    # ny, nx, nt, nit, rho, nu = (1024, 1024, 100, 20, 1.0, 0.1)
    ny, nx, nt, nit, rho, nu = (4096, 4096, 100, 20, 1.0, 0.1)
    u, v, p, dx, dy, dt = initialize(ny, nx)
    dace_u, dace_v, dace_p = u.copy(), v.copy(), p.copy()

    assert device_type in {dace.dtypes.DeviceType.CPU, dace.dtypes.DeviceType.GPU}

    # Parse the SDFG and apply autopot
    g = dace_cavity_flow.to_sdfg()
    g.save(os.path.join('_dacegraphs', 'cavity-0.sdfg'))
    g = auto_optimize(g, device_type)

    # USING ConstAssignmentStateFusion
    use_const_fusion = True
    use_gsls = False
    if use_const_fusion:
        g.apply_transformations_repeated(ConstAssignmentStateFusion,
                                         opts = {'use_grid_strided_loops': use_gsls})

    g.validate()
    instrument_map_kernels(g)
    g.save(os.path.join('_dacegraphs', 'cavity-1.sdfg'))

    g.validate()
    g.compile()

    def op():
        u, v, p, dx, dy, dt = initialize(ny, nx)
        dace_u, dace_v, dace_p = u.copy(), v.copy(), p.copy()
        g(nt=nt, nit=nit,
          u=dace_u, v=dace_v,
          dt=dt, dx=dx, dy=dy,
          p=dace_p, rho=rho,
          nu=nu, ny=ny, nx=nx)
    print('Warmup...')
    op()  # Warmup
    g.clear_instrumentation_reports()
    print('Actual...')
    for i in tqdm.trange(10):
        op()
    print(produce_combined_instrumentation_report(g, f"{'post' if use_const_fusion else 'pre'}_{device_type}.json"))

    # # Compute ground truth and Validate result
    # numpy_cavity_flow(nx, ny, nt, nit, u, v, dt, dx, dy, p, rho, nu)
    # assert (np.allclose(dace_u, u) or relerror(dace_u, u) < 1e-10)
    # assert (np.allclose(dace_v, v) or relerror(dace_v, v) < 1e-10)
    # assert (np.allclose(dace_p, p) or relerror(dace_p, p) < 1e-10)
    return g


def test_cpu():
    run_cavity_flow(dace.dtypes.DeviceType.CPU)


@pytest.mark.gpu
def test_gpu():
    run_cavity_flow(dace.dtypes.DeviceType.GPU)


@pytest.mark.skip(reason="Intel FPGA kernel arguments")
@fpga_test(assert_ii_1=False)
def test_fpga():
    run_cavity_flow(dace.dtypes.DeviceType.FPGA)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", default='cpu', choices=['cpu', 'gpu', 'fpga'], help='Target platform')

    args = vars(parser.parse_args())
    target = args["target"]

    if target == "cpu":
        run_cavity_flow(dace.dtypes.DeviceType.CPU)
    elif target == "gpu":
        run_cavity_flow(dace.dtypes.DeviceType.GPU)
    elif target == "fpga":
        run_cavity_flow(dace.dtypes.DeviceType.FPGA)

