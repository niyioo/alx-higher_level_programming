#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 *
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);

	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", bytes->ob_sval[i] & 0xff);
	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python list object
 *
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(element))
		{
			printf("bytes\n");
			print_python_bytes(element);
		}
		else if (PyFloat_Check(element))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(element))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(element))
		{
			printf("list\n");
		}
		else if (PyLong_Check(element))
		{
			printf("int\n");
		}
		else if (PyUnicode_Check(element))
		{
			printf("str\n");
		}
		else
		{
			printf("Unknown type\n");
		}
	}
}
