#include <Python.h>
#include "cdeltamodule.h"


PyObject * delta(PyObject *self, PyObject *args) {
	int num;
	char *name;

	if(!PyArg_ParseTuple(args, "is", &num, &name))
		return NULL;

	return PyUnicode_FromFormat("Hay %s!  You gave me %d.", name, num);
}
