"""
A class representing a node in a linked list
All operations are done in O(1) Space and Time complexity
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


"""
A class representing a linked list of nodes
All operations excluding __str__ are implemented in O(1) Space and Time complexity
__str__ is implemented in O(n) Time and space complexity with n being the length of the list
"""


class LinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        representation = '['
        iterator = self.head
        while iterator is not None:
            representation += str(iterator) + ','
            iterator = iterator.next_node
        return representation[:-1] + ']'

    def add(self, other: Node):
        other.next_node, self.head = self.head, other
        self.size += 1

    def remove(self, other: Node):
        # In case the node to remove is the first one AKA the head
        if other == self.head:
            self.head = self.head.next_node
            return

        # Iterating over the list searching for the value to remove
        slow_iterator = self.head
        fast_iterator = self.head.next_node
        while fast_iterator is not None:
            # Removing the node
            if fast_iterator == other:
                value = fast_iterator.value
                slow_iterator.next_node = fast_iterator.next_node
            slow_iterator = slow_iterator.next_node
            fast_iterator = fast_iterator.next_node

        self.size -= 1

    def is_empty(self) -> bool:
        return self.size == 0

