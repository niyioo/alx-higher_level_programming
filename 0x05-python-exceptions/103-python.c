#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: The PyObject pointer representing the list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, item_type);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: The PyObject pointer representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	const char *str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < 10 && i < size; ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: The PyObject pointer representing the float object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
