from scipy.integrate import quad


def integrand(x: float) -> float:
    return x ** 3


def compute_delta() -> float:
    return quad(integrand, 0, 1)[0]
