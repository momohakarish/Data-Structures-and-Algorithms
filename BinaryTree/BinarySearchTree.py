from typing import Any


"""
This class represents a node inside a tree
"""


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)



"""
This class represents a binary search tree
Average time complexity is O(log(n))
Worst time complexity is O(n)
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None

    """
    Returns the tree in a pre order
    """

    def __str__(self):
        output = ['']
        self.__pre_order(self.root, output)
        return output[0][:-1]

    def __pre_order(self, root, output):
        if root is None:
            return

        output[0] += str(root.value) + ','
        self.__pre_order(root.left, output)
        self.__pre_order(root.right, output)

    def insert(self, value):
        # If the tree is empty
        if self.root is None:
            self.root = TreeNode(value)
            return

        self.__insert(value, self.root)

    # Implementation of the insert
    def __insert(self, value, root):
        if value == root.value:
            return

        # if node is a leaf
        if root.left is None and root.right is None:
            if root.value > value:
                root.left = TreeNode(value)
            else:
                root.right = TreeNode(value)

        # If the node has only a left subtree
        elif root.left is not None and root.right is None:
            if root.value > value:
                self.__insert(value, root.left)
            else:
                root.right = TreeNode(value)

        # If the node has only a right subtree
        elif root.left is None:
            if root.value > value:
                root.left = TreeNode(value)
            else:
                self.__insert(value, root.right)

        # If the tree has both a right and a left subtree
        else:
            if root.value > value:
                self.__insert(value, root.left)
            else:
                self.__insert(value, root.right)

    def retrieve(self, value, remove=None):
        return self.__retrieve(value, remove, self.root)

    def __retrieve(self, value, remove, root):
        # If the key doesn't exist in the tree
        if root.right is None and root.left is None:
            return

        # If we found the key
        if root.value == value:
            pass
        # If the key is in the right subtree
        elif root.value > value:
            return self.__retrieve(value, remove, root.right)
        # If the key is in the left subtree
        else:
            return self.__retrieve(value, remove, root.right)


