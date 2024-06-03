from numba import jit


@jit(nopython=True)
def function_to_integrate(x):
    """Example function to integrate: f(x) = x^3"""
    return x ** 3


@jit(nopython=True)
def trapezoidal_rule(a, b, n):
    """Compute the integral of function_to_integrate from a to b using the trapezoidal rule with n intervals."""
    h = (b - a) / n
    integral = 0.5 * (function_to_integrate(a) + function_to_integrate(b))
    for i in range(1, n):
        x = a + i * h
        integral += function_to_integrate(x)
    integral *= h
    return integral


@jit(nopython=True)
def integrate(a, b, precision):
    """Compute the integral of function_to_integrate from a to b with the desired precision."""
    n = 1
    current_integral = trapezoidal_rule(a, b, n)
    while True:
        n *= 2
        new_integral = trapezoidal_rule(a, b, n)
        if abs(new_integral - current_integral) < precision:
            return new_integral
        current_integral = new_integral


@jit(nopython=True)
def compute_integral(precision):
    """Compute the integral of function_to_integrate from 0 to 1 with the given precision."""
    a = 0.0
    b = 1.0
    return integrate(a, b, precision)
