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
	long int size, i, limit;
	char *buffer;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	buffer = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);

	limit = (size < 10) ? size : 10;

	printf("  first %ld bytes:", limit);

	i = 0;
	while (i < limit)
	{
		printf(" %02x", buffer[i]);
		i++;
	}

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
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	i = 0;
	while (i < size)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		i++;
	}
}
