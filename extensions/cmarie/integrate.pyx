from libc.math cimport fabs

cdef double function_to_integrate(double x):
    return x * x

cdef double trapezoidal_rule(double a, double b, int n):
    cdef double h = (b - a) / n
    cdef double integral = 0.5 * (function_to_integrate(a) + function_to_integrate(b))
    cdef int i
    cdef double x

    for i in range(1, n):
        x = a + i * h
        integral += function_to_integrate(x)

    integral *= h
    return integral

cpdef double integrate(double a, double b, double precision):
    cdef int n = 1
    cdef double current_integral, previous_integral

    previous_integral = trapezoidal_rule(a, b, n)

    while True:
        n *= 2
        current_integral = trapezoidal_rule(a, b, n)

        if fabs(current_integral - previous_integral) < precision:
            break

        previous_integral = current_integral

    return current_integral

cpdef compute_integral():
    cdef double a = 0.0
    cdef double b = 1.0
    cdef double precision = 1e-6

    return integrate(a, b, precision)
