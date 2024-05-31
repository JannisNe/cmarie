import timeit
from functools import cache
import numpy as np

from cmarie.delta import compute_delta as delta_python


@cache
def setup_data():
    print("initialising data")
    a = np.linspace(0, 10, 2)
    b = np.linspace(0, 100, 5)
    delta_z_sonde = 4
    cw = 0.3
    tau = np.linspace(4, 9, 5)
    reff = np.linspace(3, 7, 5)
    rhow = 9
    qe = 0.06
    z_b = np.linspace(0, 0.004, 5)
    upper = np.linspace(2, 3, 5)
    lower = upper - 0.3
    return a, b, delta_z_sonde, cw, tau, reff, rhow, qe, z_b, upper, lower


def test_func(which: str):
    match which:
        case "python":
            fct = delta_python
        case _:
            raise ValueError(f"'{which}' not known!")

    print(f"testing {which}")
    _data = setup_data()

    def _testfunc():
        return fct(*_data)

    print("running ...")
    timer = timeit.Timer(_testfunc)
    auto_n, _ = timer.autorange()
    print(f" {auto_n} x 5 times ....")
    times = np.array(timer.repeat(number=auto_n, repeat=10)) / auto_n
    val = _testfunc()
    print(
        f"------------ {which} ------------ \n"
        f"  Result: {val}"
        f"  Min:  {min(times):.2e}s\n"
        f"  Max:  {max(times):.2e}s\n"
        f"  Mean: {np.mean(times):.2e}s +/- {np.std(times):.2e}s\n\n"
    )


if __name__ == '__main__':
    for which in ["python", "c", "cython"]:
        test_func(which)
