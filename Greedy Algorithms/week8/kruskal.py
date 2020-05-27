"""
Kruskal MST
-sort edges by weight
-pick edge with minimal weight
-if this edge doen't create cycle add to MST
-repeat until all vertex appear in MSG
"""

"""
INPUT graph and weights
 -----1----
| 1   |  1 |
0     |1    2
| 3   |  2 |
 -----3----

"""

graph = {
    0: {1:1, 3:3},
    1: {0:1, 2:1, 3:1},
    2: {1:1, 3:2},
    3: {0:3, 1:1, 2:2},
}

class Union:
    pass

from dataclasses import dataclass

@dataclass
class Edge:
    """
    weighted edge
    """
    weight: int
    start: int
    end: int

    def __lt__(self, other):
        return self.weight < other.weight


def kruskal_brute(graph):
    """
    1. Sort edges by weight
    2. Assing each graph vertex unique id
    3. For every min edge added to result
       - update all associated ids to tail_id
    """
    # (weight, start, end)
    all_edges = []
    for start in graph:
        for tail in graph[start]:
            all_edges.append(Edge(graph[start][tail], start, tail))
    sorted_edges = sorted(all_edges)

    #Can be optimized with DSU
    explored = {k:k for k in graph}

    result = []
    for edge in sorted_edges:
        if explored[edge.start] != explored[edge.end]:
            old_id = explored[edge.start]
            for key in explored:
                if explored[key] == old_id:
                    explored[key] = explored[edge.end]
            result.append(edge)
    print(result)

from dsu import DSU
def kruskal(graph):
    """
    Use union-find
    """
    all_edges = []
    for start in graph:
        for tail in graph[start]:
            all_edges.append(Edge(graph[start][tail], start, tail))
    sorted_edges = sorted(all_edges)

    dsu = DSU(len(graph)+1)
    result = []

    for edge in sorted_edges:
        if dsu.find_set(edge.start) != dsu.find_set(edge.end):
            dsu.union_sets(edge.start, edge.end)
            result.append(edge)
    print(result)

def clustering(graph, k):
    """
    Use union-find
    """
    all_edges = []
    for start in graph:
        for tail in graph[start]:
            all_edges.append(Edge(graph[start][tail], start, tail))
    sorted_edges = sorted(all_edges)

    dsu = DSU(len(graph)+1)
    result = []

    num_clusters = len(graph)
    for edge in sorted_edges:
        if dsu.find_set(edge.start) != dsu.find_set(edge.end):
            if num_clusters == k:
                print(edge)
                return
            dsu.union_sets(edge.start, edge.end)
            result.append(edge)
            num_clusters -=1


from collections import defaultdict
def test_quiz1(input):
    graph = defaultdict(dict)
    with open(input) as file:
        nodes = file.readline().split()

        for line in file:
            start,end,weight = map(int, line.split())
            graph[start][end] = weight
            graph[end][start] = weight

    clustering(graph, 4)


# test_quiz1('quiz1')






