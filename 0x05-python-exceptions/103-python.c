#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyObject_Length(p);
	const char *string = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first 6 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 6; i++)
	{
		printf("%02x", (unsigned char)string[i]);
		if (i + 1 < size && i + 1 < 6)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyObject_Length(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, typeName);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: Pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf("  value: %.17g\n", value);
}
