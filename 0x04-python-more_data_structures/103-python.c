#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
	printf("[*] Allocated = %ld\n", list->allocated);

	size = Py_SIZE(list);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(list, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;
	unsigned char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", Py_SIZE(bytes));
	printf("  trying string: %s\n", Py_TYPE(bytes)->tp_name);

	size = Py_SIZE(bytes);
	printf("  first %ld bytes: ", (size > 10) ? 10 : size);

	str = (unsigned char *)PyBytes_AS_STRING(bytes);
	for (i = 0; i < ((size > 10) ? 10 : size); i++)
	{
		printf("%02x", str[i]);
		if (i < ((size > 10) ? 9 : size - 1))
			printf(" ");
	}
	printf("\n");
}
