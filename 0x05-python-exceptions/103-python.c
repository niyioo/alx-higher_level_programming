#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: The PyObject pointer representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i, bytes_size, j;
	PyObject *item;
	const char *item_type;
	const char *str;
	double value;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, item_type);

		if (PyBytes_Check(item))
		{
			printf("[.] bytes object info\n");
			bytes_size = PyBytes_Size(item);
			printf("  size: %zd\n", bytes_size);

			str = PyBytes_AsString(item);
			printf("  trying string: %s\n", str);

			printf("  first 6 bytes: ");
			for (j = 0; j < 6 && j < bytes_size; ++j)
			{
				printf("%02x ", (unsigned char)str[j]);
			}
			printf("\n");
		}
		else if (PyFloat_Check(item))
		{
			printf("[.] float object info\n");
			value = PyFloat_AsDouble(item);
			printf("  value: %f\n", value);
		}
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: The PyObject pointer representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	const char *str;
	Py_ssize_t i;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first 6 bytes: ");
	for (i = 0; i < 6 && i < size; ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("00\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: The PyObject pointer representing the float object
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
