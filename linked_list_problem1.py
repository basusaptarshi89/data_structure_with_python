# Problem Statement:
#
# You have two numbers represented by linked list, where each node contains a single digit.
# The digits are stored in forward order. Write a function that adds the two numbers and returns
# the sum as a linked list.
# Example:
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5)
# Output: 9 -> 1 -> 2 (617 + 195 = 912)
import linked_list

def convert_list2number(list):
    """
    Converts linked list representation to number
    :param list: Linked List object; 6 -> 1 -> 7
    :return: number: 617
    """
    sum = 0
    current = list.head
    while current:
        sum = sum*10 + current.data
        current = current.next
    return sum

def convert_number2list(number):
    """
    Converts number to linked list representation
    :param number: 617
    :return: number: Linked List object; 6 -> 1 -> 7
    """
    list = linked_list.LinkedList()
    while number != 0:
        remainder = number % 10
        number = number // 10
        list.add_at_beginning(remainder)
    return list

def add_lists(list1, list2):
    num1 = convert_list2number(list1)
    num2 = convert_list2number(list2)
    sum = num1 + num2
    return convert_number2list(sum)


# UNIT TESTING

linked_list_1 = linked_list.LinkedList()
linked_list_1.add(6)
linked_list_1.add(1)
linked_list_1.add(7)

linked_list_2 = linked_list.LinkedList()
linked_list_2.add(2)
linked_list_2.add(9)
linked_list_2.add(5)

print('Function: convert_list2number')
print(f'List 1: {linked_list_1}')
print(f'Number: {convert_list2number(linked_list_1)}')
print()

print('Function: convert_list2number')
print(f'List 2: {linked_list_2}')
print(f'Number: {convert_list2number(linked_list_2)}')
print()

print('Function: convert_number2list')
print(f'Number: {123}')
print(f'List: {convert_number2list(123)}')
print()

print('Function: add_lists')
print(f'List1: {linked_list_1}')
print(f'List2: {linked_list_2}')
print(f'Sum list: {add_lists(linked_list_1, linked_list_2)}')