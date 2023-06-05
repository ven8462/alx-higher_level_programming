#include "lists.h"

/**
 * check_cycle - Detects if there is a cycle in a linked list.
 * @head: The head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *head)
{
	/* Initializie the s_runner and f_runner pointers to the head of the list*/
	listint_t *slow_runner = head;
	listint_t *fast_runner = head;

	/* Loop until the f_runner reaches the end of the list/its next node is NULL*/
	while (fast_runner != NULL && fast_runner->next != NULL)
	{
		/* Move the slow_runner pointer one step forward */
		slow_runner = slow_runner->next;
		/* Move the fast_runner pointer two steps forward */
		fast_runner = fast_runner->next->next;

		/* Check if the slow_runner and fast_runner pointers meet at some point*/
		if (slow_runner == fast_runner)
		{
			/* If they meet, it means there is a cycle in the linked list */
			return (1);
		}
	}

	/* If the f_runner  reaches the end of the list/its next node is NULL*/
	/* it means there is no cycle in the linked list */
	return (0);
}
