"""
Huffman codes
Encoding bit strings
    - based on prefix free binary trees
    - merge 2 lowest as 1 tree, sum their weights

"""
# Ex.
# Input {A, B, C, D} -> frequency 60, 25, 10, 5
# Output: comput prefix binary tree

from dataclasses import dataclass
from typing import Optional
@dataclass
class Node:
    #tree
    left: Optional['Node']
    right: Optional['Node']

    #data
    key: str
    value: int

    def __lt__(self, other):
        return self.value < other.value

    def print(self, codes):
        if not self.left and not self.right:
            print(f"{self.key}:{self.value}", codes, "  ", len(codes))
        if self.left:
            self.left.print(codes + "0")
        if self.right:
            self.right.print(codes + "1")

    def min(self, number):
        if not self.left and not self.right:
            return number

        left = float('inf')
        right = float('inf')
        if self.left:
            left = self.left.min(number+1)
        if self.right:
            right = self.right.min(number+1)

        return min(left, right)

    def max(self, number):
        if not self.left and not self.right:
            return number

        left = float('-inf')
        right = float('-inf')
        if self.left:
            left = self.left.max(number+1)
        if self.right:
            right = self.right.max(number+1)

        return max(left, right)

def merge(node1, node2):
    return Node(node1, node2, "special", node1.value + node2.value)

def print_huffman(tree):
    codes = ""
    tree.print(codes)

def print_min(tree):
    print(tree.min(0))

def print_max(tree):
    print(tree.max(0))

from heapq import heappush, heappop, heapify
def huffman(input):
    """
    - Create tree nodes from each entry
    - Place everything to heap
    - Extract 2 min nodes
    """
    heap = [Node(None, None, k, v) for k,v in input.items()]
    heapify(heap)

    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)
        internal_node = merge(node1, node2)

        heappush(heap, internal_node)

    tree = heappop(heap)
    return tree

def test1():
    data ={'A':60, 'B':25, 'C':10, 'D':5}
    tree = huffman(data)
    print_huffman(tree)
    print_min(tree)
    print_max(tree)

def test2():
    data = {'a': 5, 'b': 9,'c': 12,'d': 13,'e': 16,'f': 45}
    tree = huffman(data)
    print_huffman(tree)
    print_min(tree)
    print_max(tree)

def quiz1():
    data = {}
    with open('quiz1') as input:
        number = input.readline()

        for idx, line in enumerate(input, 1):
            data[idx] = int(line)
    tree = huffman(data)
    print_huffman(tree)
    print_min(tree)
    print_max(tree)

test1()
test2()
quiz1()
