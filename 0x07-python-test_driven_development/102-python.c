#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 */

void print_python_string(PyObject *p)
{
	PyUnicodeObject *unicode_obj;
	PyBytesObject *bytes_obj;

	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		unicode_obj = (PyUnicodeObject *)p;
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString((PyObject *)unicode_obj, NULL));
	}
	else if (PyBytes_Check(p))
	{
		bytes_obj = (PyBytesObject *)p;
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", PyBytes_GET_SIZE(p));
		printf("  value: %s\n", PyBytes_AS_STRING(bytes_obj));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
