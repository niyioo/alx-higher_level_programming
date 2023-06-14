#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list
 * @p: Pointer to the PyObject representing the Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to the PyObject representing the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	const char *string = PyBytes_AS_STRING(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}
