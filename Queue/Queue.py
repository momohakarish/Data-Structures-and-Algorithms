from typing import Any


"""
A queue implementation using a dynamic array
All actions are preformed in O(1) Time Complexity despite dequeue and __str__ which are O(n)
All actions are preformed in O(1) Space complexity despite __Str__ which is O(n)
"""


class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self) -> int:
        return len(self.queue)

    def __str__(self) -> str:
        return str(self.queue)

    def enqueue(self, item: Any):
        self.queue.append(item)

    def dequeue(self) -> Any:
        if len(self.queue) == 0:
            raise IndexError('Attempted dequeue from an empty queue')
        value = self.queue[0]
        self.queue.remove(value)
        return value

    def peek(self) -> Any:
        if len(self.queue) == 0:
            raise IndexError('Attempted peek from an empty queue')
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

