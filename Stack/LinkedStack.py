"""
A class representing a node in a linked list
All operations are done in O(1) Space and Time complexity
"""
from typing import Any


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    """
    Returns weather the node is pointing to another node
    """
    def has_next(self) -> bool:
        return self.next_node is not None


"""
A class representing a stack implemented with a linked list
All operations excluding __str__ are implemented in O(1) Space and Time complexity
__str__ is implemented in O(n) Time and space complexity with n being the length of the list
"""


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    """
    The top of the stack is the first element to be printed
    We represent the top of the stack with the head node
    """
    def __str__(self) -> str:
        iterator = self.head
        output = '['
        while iterator is not None:
            output += str(iterator.value) + ','
            iterator = iterator.next_node
        return output[:-1] + ']'

    def push(self, value):
        # Creating a node from the value so we can add it to our list
        other = Node(value)
        # Adding the node to our list
        other.next_node, self.head = self.head, other
        self.size += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Attempted pop from an empty stack')
        return_value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return return_value

    def peek(self) -> Any:
        return self.head.value

    def is_empty(self) -> bool:
        return self.size == 0

a = LinkedStack()
a.push(25)
a.push(42)
print(a)
print(len(a))
print(a.pop())
print(a.pop())
print(a.is_empty())

