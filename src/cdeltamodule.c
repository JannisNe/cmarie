#include <Python.h>
#include "cdeltamodule.h"


// Function to compute the value of a polynomial
double compute_polynomial(double x) {
    double result = x * x * x;
    return result;
}


// Function to integrate another function using the trapezoidal rule
double integrate(double (*func)(double), double a, double b, int n) {
    double h = (b - a) / n; // Step size
    double integral = 0.5 * (func(a) + func(b)); // Initialize integral with the first and last terms

    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        integral += func(x);
    }

    integral *= h; // Multiply by the step size to get the final integral value
    return integral;
}


PyObject * compute_integral() {
    double result = integrate(compute_polynomial, 0.0, 1.0, 1000000);
    return Py_BuildValue("d", result);
}
