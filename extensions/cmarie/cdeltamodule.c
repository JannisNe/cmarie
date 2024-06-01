#include <Python.h>
#include <math.h>
#include "cdeltamodule.h"


// Function to compute the value of a polynomial
double compute_polynomial(double x) {
    double result = x * x * x;
    return result;
}


// Function to integrate another function using the trapezoidal rule with adaptive step size
double integrate(double (*func)(double), double a, double b, double rel_precision) {
    int n = 1; // Start with one interval
    double current_integral, previous_integral;
    double h, x;

    previous_integral = (func(a) + func(b)) * (b - a) / 2.0; // Initial approximation with one interval

    do {
        n *= 2; // Double the number of intervals
        h = (b - a) / n; // New step size
        current_integral = 0.5 * (func(a) + func(b)); // Re-initialize integral with the first and last terms

        for (int i = 1; i < n; i++) {
            x = a + i * h;
            current_integral += func(x);
        }

        current_integral *= h; // Multiply by the step size to get the final integral value

        // Check if the change in the integral value is within the desired precision
        if ((fabs(current_integral - previous_integral) / previous_integral) < rel_precision) {
            break;
        }

        previous_integral = current_integral;

    } while (1);

    return current_integral;
}



PyObject * compute_integral() {
    double result = integrate(compute_polynomial, 0.0, 1.0, 1e-6);
    return Py_BuildValue("d", result);
}
