"""
Disjoint set implementation
Three operations:

    - make_set(v) - creates a new set with element v
    - union_sets(a, b) - merges the two specified sets (the set in which the element a is located, and the set in which the element b is located)
    - find_set(v) - returns the representative (also called leader) of the set that contains the element v. This representative is an element of its corresponding set. It is selected in each set by the data structure itself (and can change over time, namely after union_sets calls). This representative can be used to check if two elements are part of the same set of not. a and b are exactly in the same set, if find_set(a) == find_set(b). Otherwise they are in different sets.
"""

class DSU:
    """
    Naive implementation:
        Each element has parent, multiple elements with same parent form a set

    Adding:
        ranks - determined on number of hops to get to the parent for the set

    Adding:
        find_set - update parents[v] each time visit elements

    """
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def make_set(self, v):
        self.parents[v] = v

    def find_set(self, v):
        if v == self.parents[v]:
            return v
        self.parents[v] = self.find_set(self.parents[v])
        return self.parents[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.rank[a] > self.rank[b]:
                self.parents[b] = a
            elif self.rank[a] == self.rank[b]:
                self.parents[b] = a
                self.rank[a] += 1
            else:
                self.parents[a] = b

def test():
    # items = [0,1,2,3,4,5]

    dsu = DSU(6)

    dsu.union_sets(0,1)

    assert dsu.parents == [0,0,2,3,4,5]

    dsu.union_sets(3,4)
    assert dsu.parents == [0,0,2,3,3,5]

    dsu.union_sets(1,3)
    assert dsu.parents == [0,0,2,0,3,5]


if __name__ == '__main__':
    test()
