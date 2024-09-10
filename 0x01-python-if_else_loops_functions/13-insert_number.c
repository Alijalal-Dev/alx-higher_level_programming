#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number sorted in a list
 * @head: the header of list
 * @number: the number to be added
 * Return: 0 if no cycle, or 1 if there is cycle
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
