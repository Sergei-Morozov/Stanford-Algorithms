"""
Calculate:
    - sum of medians mod 1000 from 1 to 10000
    - as example median(5) is median of 5 first elements
input:
    - list of the integers from 1 to 10000 in unsorted order
"""

import math

heap = [4,4,8,9,4,12,9,11,7]

def less(x,y):
    return x < y

def greater(x,y):
    return x >= y

class Heap():
    def __init__(self, heap, compare = less):
        self.heap = heap
        self.compare = compare

    def balance_down(self):
        """
        Balance heap on from root position
        -bubble-down
        """
        i = 0
        left = 2*i + 1
        right = 2*i + 2
        while left < len(self.heap):
            if right < len(self.heap) and self.compare(self.heap[right], self.heap[left]):
                self.heap[i],self.heap[right] = self.heap[right],self.heap[i]
                i = right
            else:
                self.heap[i],self.heap[left] = self.heap[left],self.heap[i]
                i = left

            left = 2*i + 1
            right = 2*i + 2

    def balance_up(self):
        """
        Balance heap on from last position
        -bubble-up
        """
        root = 0
        i = len(self.heap)-1

        while i > root:
            # parent index
            parent = (i-1) >> 1
            # swap value
            if self.compare(self.heap[i], self.heap[parent]):
                self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            i = parent


    def push(self, k):
        """
        -insert to end
        -rebalance on k
        """
        self.heap.append(k)
        self.balance_up()


    def pop(self):
        """
        - delete root
        - move last to root
        - balance
        """
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.balance_down()
            return root

    def get(self):
        """
        Return heap min/max value
        """
        return self.heap[0]

    def size(self):
        return len(self.heap)


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



class StreamingMedian:
    """
    Streaming median based on integer input
    """
    def __init__(self):
        self.left_heap = Heap([], greater)
        self.right_heap = Heap([], less)

    def get_median(self, input):
        """
        Calculate streaming median based on previous inputs
        to lef
        """

        if self.left_heap.size() == 0:
            self.left_heap.push(input)
            return input
        else:
            # push to right heap
            if input < self.left_heap.get():
                self.left_heap.push(input)
            else:
                self.right_heap.push(input)

            #balance
            balance = self.left_heap.size() - self.right_heap.size()

            if balance > 1:
                self.right_heap.push(self.left_heap.pop())
            if balance < -1:
                self.left_heap.push(self.right_heap.pop())

            #median
            if self.left_heap.size() < self.right_heap.size():
                return self.right_heap.get()
            else:
                return self.left_heap.get()



def test():
    input = [9,9,7,1,2,3,4,5,6,7,8,9]
    result = 0
    median = StreamingMedian()
    for x in input:
        result += median.get_median(x)
    assert result%len(input) == 2

# test()


def quiz2():
    with open("quiz2") as input:
        median = StreamingMedian()
        result = 0
        lines = []
        for line in input:
            lines.append(line)
        for line in lines[:]:
            result += median.get_median(int(line))
        print(result)

quiz2()

heap1 = [4292, 1640, 3611, 625, 4135, 3480, 2303, 225, 1260, 1354, 1386, 1446, 2793]
heap2 = [4479, 5147, 5685, 7600, 6193, 6331, 6447, 9290, 9046, 6195, 7293, 8583]

# median = StreamingMedian()
# median.left_heap.heap = heap1
# median.right_heap.heap = heap2

# print(median.get_median(2022))
# show_tree(median.left_heap.heap)
# show_tree(median.right_heap.heap)

heap = Heap([], greater)
for h in heap1:
    heap.push(h)

for _ in range (6):
    heap.pop()

show_tree(heap.heap)








