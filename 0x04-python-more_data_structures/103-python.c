#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes object information
 *
 * @p: Python bytes object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	unsigned char *buffer;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	buffer = (unsigned char *)PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);

	limit = (size < 10) ? size : 10;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", buffer[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list object information
 *
 * @p: Python list object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;
	PyObject *item;

	size = PyList_Size(p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
