"""
A stack implementation using a list
All operations with the exception of __str__ are done in O(1) Time and Space complexity
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __len__(self) -> int:
        return self.size

    """
    The Top of the stack is the last element to be printed
    """
    def __str__(self) -> str:
        return str(self.stack)

    def push(self, other):
        # The last element in the list is the top of the stack
        self.stack.append(other)
        self.size += 1

    def pop(self) -> Any:
        if self.size == 0:
            raise IndexError('Attempted pop from an empty stack')
        self.size -= 1
        return self.stack.pop()

    def peek(self) -> Any:
        if self.size > 0:
            return self.stack[-1]

    def is_empty(self) -> bool:
        return self.size == 0
