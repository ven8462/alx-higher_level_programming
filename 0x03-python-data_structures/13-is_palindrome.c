#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list to be reversed
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list to be checked
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	prev_slow->next = NULL;
	listint_t *second_half = reverse_list(slow);
	listint_t *second_half_copy = second_half;

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			reverse_list(second_half_copy);
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_list(second_half_copy);
	return (1);
}
