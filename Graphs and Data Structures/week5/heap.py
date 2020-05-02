"""
Implementation of heap
- heapify
- heappush
- heappop

Reside in list like tree levels ordered from 0 -- 1 level -- 2 level --- level 3
- parent in position i/2 -> (i-1) >> 1
- children in position  are 2i, 2i+1 -> with 0 index its 2i+1 and 2i+2
"""
import math

heap = [4,4,8,9,4,12,9,11,7]

def balance_down(heap):
    """
    Balance heap on from root position
    -bubble-down
    """
    i = 0
    left = 2*i + 1
    right = 2*i + 2
    while left < len(self.heap):
        if right < len(self.heap) and self.heap[right] <self.heap[left]:
            self.heap[i],self.heap[right] = self.heap[right],self.heap[i]
            i = right
        else:
            self.heap[i],self.heap[left] = self.heap[left],self.heap[i]
            i = left
        left = 2*i + 1
        right = 2*i + 2



def balance_up(heap):
    """
    Balance heap on from last position
    -bubble-up
    """
    root = 0
    i = len(heap)-1

    while i > root:
        # parent index
        parent = (i-1) >> 1
        # swap value
        if heap[i] < heap[parent]:
            heap[i],heap[parent] = heap[parent],heap[i]
        i = parent


def heappush(heap, k):
    """
    -insert to end
    -rebalance on k
    """
    heap.append(k)
    balance_up(heap)


def heappop(heap):
    """
    - delete root
    - move last to root
    - balance
    """
    root = heap[0]
    heap[0] = heap.pop()
    balance_down(heap)
    return root

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    import math
    from io import StringIO
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

show_tree(heap)
