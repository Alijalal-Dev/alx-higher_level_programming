#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: A pointer to the Python list to print information about
 */
void print_python_list_info(PyObject *p)
{
	long int size = Py_SIZE(p), idx = 0;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (; idx < size; ++idx)
	{
		printf("Element %ld: %s\n", idx,
		Py_TYPE(((PyListObject *)p)->ob_item[idx])->tp_name);
	}
}
