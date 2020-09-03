class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def has_next(self) -> bool:
        return self.next_node is not None


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.size = 0
        if self.head is not None:
            self.size = 1

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        representation = '['
        iterator = self.head
        while iterator is not None:
            representation += str(iterator) + ','
            iterator = iterator.next_node
        return representation[:-1] + ']'

    # Adding a node to the list
    def add(self, other: Node):
        other.next_node, self.head = self.head, other
        self.size += 1

    # Removing a node from the list
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
                slow_iterator.next_node = fast_iterator.next_node
            slow_iterator = slow_iterator.next_node
            fast_iterator = fast_iterator.next_node

        self.size -= 1

    # Returning if the list is empty or not
    def is_empty(self) -> bool:
        return self.size == 0



a = LinkedList()
a.add(Node(5))
a.add(Node(23))
a.add(Node(45))
a.remove(Node(5))
print(a)
print(a.pop())
print(a)