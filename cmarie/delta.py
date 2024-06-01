from scipy.integrate import quad


def integrand(x: float) -> float:
    return x ** 3


def compute_integral() -> float:
    return quad(integrand, 0, 1, epsrel=1e-6)[0]
