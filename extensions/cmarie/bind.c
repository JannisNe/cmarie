#include "cdeltamodule.h"

static PyMethodDef cdelta_funcs[] = {
	{	"compute_integral",
		(PyCFunction)compute_integral,
		METH_VARARGS,
		NULL},
		{NULL, NULL, 0, NULL}
};

static struct PyModuleDef cdelta_mod = {
	PyModuleDef_HEAD_INIT,
	"cdelta",
	"q2d",
	-1,
	cdelta_funcs,
};

PyMODINIT_FUNC PyInit_cdelta(void) {
	return PyModule_Create(&cdelta_mod);
};