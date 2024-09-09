#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - check for the loop in a linked list
 * @list: data type listint_t pointer of list
 * Return: 0 if no cycle || 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
