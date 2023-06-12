# Project 0x03. Python - Data Structures: Lists, Tuples
# Description
This project focuses on working with lists and tuples in Python. It consists of several functions that perform operations on lists and tuples, such as printing integers, accessing elements, replacing elements, reversing lists, removing characters from strings, printing matrices, adding tuples, and finding the maximum integer in a list.

# The project includes the following files:

0-print_list_integer.py: Contains a function print_list_integer(my_list) that prints all the integers of a given list.

1-element_at.py: Contains a function element_at(my_list, idx) that retrieves an element from a list based on the given index.

2-replace_in_list.py: Contains a function replace_in_list(my_list, idx, element) that replaces an element in a list at a specific position.

3-print_reversed_list_integer.py: Contains a function print_reversed_list_integer(my_list) that prints all the integers of a list in reverse order.

4-new_in_list.py: Contains a function new_in_list(my_list, idx, element) that replaces an element in a list at a specific position without modifying the original list.

5-no_c.py: Contains a function no_c(my_string) that removes all occurrences of the character 'c' and 'C' from a given string.

6-print_matrix_integer.py: Contains a function print_matrix_integer(matrix) that prints a matrix of integers.

7-add_tuple.py: Contains a function add_tuple(tuple_a, tuple_b) that adds two tuples together.

8-multiple_returns.py: Contains a function multiple_returns(sentence) that returns a tuple with the length of a string and its first character.

9-max_integer.py: Contains a function max_integer(my_list) that finds the biggest integer in a list.

# Usage
Each file is a standalone module and can be executed independently. You can import the functions into your own Python scripts and use them as needed. The usage of each function is described below:

# 0-print_list_integer.py
This module provides the function print_list_integer(my_list). It takes a list of integers as input and prints each integer on a separate line.

# Example usage:

# python example

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
# Output:

1
2
3
4
5
# 1-element_at.py
This module provides the function element_at(my_list, idx). It retrieves an element from a list based on the given index.

# Example usage i python:
my_list = [1, 2, 3, 4, 5]
idx = 3
element = element_at(my_list, idx)
print("Element at index {:d} is {}".format(idx, element))
# Output:
Element at index 3 is 4
# 2-replace_in_list.py
This module provides the function replace_in_list(my_list, idx, element). It replaces an element in a list at a specific position.

# Example usage in python:
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
# Output:
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
