"""
Binary search tree
- E node has ptr to left/right/parent
- all keys on left subtree is less then right subtree

Opertions:
-search
-balance
-inserts
    -search
    -rewrite last NULL
precessor
    - previous smallest element
-delete
    - simple just delete
    - 1 child - swap
    - 2 children - get l=precessor(k), swap k and l
-select
    - number
-rank

"""

from dataclasses import dataclass

@dataclass
class Node:
    """
    Represents tree node
    """
    left: "Node" = None
    right: "Node" = None

    # value
    value: int = None

    def insert(self, value):
        """
        Insert element to tree
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(None, None, value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(None, None, value)
            else:
                self.right.insert(value)

    def find(self, value):
        """
        Find element in tree
        """
        if self.value == value:
            return value
        elif value < self.value :
            if self.left:
                return self.left.find(value)
            return None
        elif value > self.value :
            if self.right:
                return self.right.find(value)
            return None

    def print(self):
        if self.left:
            self.left.print()
        print(self.value)
        if self.right:
            self.right.print()

@dataclass
class Tree:
    """
    Tree, has only rootNode
    """
    root: Node = None

    def add_value(self, value):
        self.root.insert(value)

    def print(self):
        self.root.print()

    def find(self, value):
        return self.root.find(value)

"""
   10
9     25
"""
tree = Tree(Node(None, None, 10))
tree.add_value(9)
tree.add_value(25)
print(tree.find(111))
tree.print()
