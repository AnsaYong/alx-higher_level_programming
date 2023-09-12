#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the start of the linked list
 *
 * Return: pointer to the new reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

    return (prev);
}

/**
 * is_palindrome - compares the first half and the reversed second half to
 * check if the linked list is a palindrome.
 * @head: pointer to a pointer to the start of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	/* An empty list or a list with a single node is a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle of the linked list using fast and slow pointers */
    while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

    /* If the list has an odd number of nodes, move slow one step ahead */
	if (fast != NULL)
		slow = slow->next;
	/* Reverse the second half of the linked list */
	second_half = reverse_list(slow);
	/* Compare the first half and the reversed second half */
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
    /* Restore the original linked list */
	prev_slow->next = reverse_list(prev_slow->next);

    return (is_palindrome);
}
