import timeit
import numpy as np

from cmarie.delta import compute_integral as python_integrate
from cmarie.cdelta import compute_integral as c_integrate
from cmarie.integrate import compute_integral as cython_integrate
from cmarie.numba_compiled import compute_integral as numba_integrate


def test_func(which: str):
    match which:
        case "python":
            fct = python_integrate
        case "c":
            fct = c_integrate
        case "cython":
            fct = cython_integrate
        case "numba":
            fct = numba_integrate
        case _:
            raise ValueError(f"'{which}' not known!")

    print(f"testing {which}")

    print("running ...")

    def _f():
        return fct(1e-4)

    timer = timeit.Timer(_f)
    auto_n, _ = timer.autorange()
    print(f" {auto_n} x 5 times ....")
    times = np.array(timer.repeat(number=auto_n, repeat=10)) / auto_n
    val = _f()
    print(
        f"------------ {which} ------------ \n"
        f"  Result: {val}\n"
        f"  Min:  {min(times):.2e}s\n"
        f"  Max:  {max(times):.2e}s\n"
        f"  Mean: {np.mean(times):.2e}s +/- {np.std(times):.2e}s\n\n"
    )


if __name__ == '__main__':
    for which in ["numba", "cython",  "python", "c"]:
        test_func(which)
