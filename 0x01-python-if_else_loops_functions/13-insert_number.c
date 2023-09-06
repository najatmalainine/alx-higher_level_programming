#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The integer to be inserted.
 *
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;
	
	/* Create a new node with the given number */
	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL); /* if memory allocation failed */

	new_node->n = number;
	new_node->next = NULL;

	/* Special case: if the list is empty or the new */
	/* node should be inserted at the beginning */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the */
	/*appropriate position to insert the new node */



	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Insert the new node after 'current' */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
