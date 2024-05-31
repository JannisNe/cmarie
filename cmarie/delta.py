from scipy.integrate import quad
import numpy.typing as npt
import numpy as np
import time
from tqdm import tqdm


def lwp1(
        delta_z_sonde: float,
        a: float,
        b: float,
        cw: float
) -> float:
    time.sleep(0.001)
    return delta_z_sonde + (a * b * cw)


def lwp2(
        tau: npt.NDArray,
        reff: npt.NDArray,
        rhow: float,
        qe: float,
        delta_z_sonde: float,
        a: float,
        b: float,
        int_val: npt.NDArray
):
    time.sleep(0.002)
    return tau * reff * rhow * qe * delta_z_sonde * a * b * int_val


def integ(
        x: float,
        a: float,
        b: float,
        z_b: float
):
    time.sleep(0.000)
    return x * a * b * z_b


def delta(
        n: npt.NDArray,
        m: npt.NDArray
):
    time.sleep(0.001)
    return n * sum(m)


def compute_delta(
        a: npt.NDArray,
        b: npt.NDArray,
        delta_z_sonde: float,
        cw: float,
        tau: npt.NDArray,
        reff: npt.NDArray,
        rhow: float,
        qe: float,
        z_b: npt.NDArray,
        upper: npt.NDArray,
        lower: npt.NDArray
) -> npt.NDArray:
    _delta = []
    for ia in a:
        for ib in b:
            _lwp1 = lwp1(delta_z_sonde, ia, ib, cw)
            _integrals = np.array([quad(integ, u, l, args=(ia, ib, iz_b))[0] for u, l, iz_b in zip(upper, lower, z_b)])
            _lwp2 = lwp2(tau, reff, rhow, qe, delta_z_sonde, ia, ib, _integrals)
            _delta.append(delta(_lwp1, _lwp2))
    return np.array(_delta)
