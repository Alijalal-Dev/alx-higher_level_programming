#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * rec_palindrome - Check if a linked list is a palindrome recursively
 * @head: A pointer to the head of the linked list
 * @tail: A pointer to the tail of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int rec_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (rec_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: A pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL && *head == NULL)
		return (1);
	else
		return (rec_palindrome(head, *head));
}
