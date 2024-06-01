from scipy.integrate import quad


def integrand(x: float) -> float:
    return x ** 3


def compute_integral(epsrel) -> float:
    return quad(integrand, 0, 1, epsrel=epsrel)[0]
