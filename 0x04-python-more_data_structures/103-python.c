#include <stdio.h>
#include <Python.h>


/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to a PyObject representing the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char size, c;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (c = 0; c < size; c++)
	{
		printf("%02hhx", bytes->ob_sval[c]);
		if (c == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}


/**
 * print_python_list - Prints information about a Python list.
 * @p: A pointer to a PyObject representing the Python list.
 */
void print_python_list(PyObject *p)
{
	long int size = 0, i = 0;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
