#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int list_length, list_allocated, index;
	PyObject *element;

	list_length = Py_SIZE(p);
	list_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_length);
	printf("[*] Allocated = %d\n", list_allocated);

	for (index = 0; index < list_length; index++)
	{
		printf("Element %d: ", index);

		element = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}

