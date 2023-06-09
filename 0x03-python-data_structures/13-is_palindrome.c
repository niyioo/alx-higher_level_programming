#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *prev_slow_ptr;
	listint_t *second_half, *mid_node;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	slow_ptr = *head;
	fast_ptr = *head;
	prev_slow_ptr = *head;
	mid_node = NULL;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	second_half = slow_ptr;
	prev_slow_ptr->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);
	if (mid_node != NULL)
	{
		prev_slow_ptr->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow_ptr->next = second_half;
	}
	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	listint_t *temp1 = list1;
	listint_t *temp2 = list2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
