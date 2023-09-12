#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_pal(head, *head));
}

/**
 * aux_pal - function to know if it is palindrome
 * @head: head list
 * @end: end list
 * Return: 0 if not, 1 if palindrome
 */

int aux_pal(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_pal(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
