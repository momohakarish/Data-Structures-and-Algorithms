"""
This implementation is better than the dynamic array implementation as it has better time and space complexity
A queue implementation using a Linked list
All operations are done in O(1) Space and Time complexity except for __str__
"""


from typing import Any

"""
A class representing a node in a linked list
"""


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


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        output = '['
        iterator = self.head
        while iterator is not None:
            output += str(iterator.value) + ', '
            iterator = iterator.next_node
        return output[:-2] + ']'

    def enqueue(self, item: Any):
        # Special case in case the queue is empty
        if self.head is None:
            self.head = self.last = Node(item)
        else:
            self.last.next_node = Node(item)
            self.last = self.last.next_node
        self.size += 1

    def dequeue(self) -> Any:
        if self.size == 0:
            raise ValueError('Attempted dequeue from empty queue')
        output = self.head
        self.head = self.head.next_node
        self.size -= 1
        return output.value

    def peek(self) -> Any:
        if self.size == 0:
            raise ValueError('Attempted peek from an empty queue')
        return self.head.value

    def is_empty(self) -> bool:
        return self.size == 0

