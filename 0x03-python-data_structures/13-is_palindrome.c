#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked-list
 * Return: 1 if a palindrome. 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	/*if (!head || !*head)*/
	/*	return (1);*/

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *reversed_half = NULL;
	listint_t *temp;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = reversed_half;
		reversed_half = temp;
	}

	if (fast)
		slow = slow->next;

	while (reversed_half && slow)
	{
		if (reversed_half->n != slow->n)
			return (0);

		reversed_half = reversed_half->next;
		slow = slow->next;
	}

	return (1);
}
