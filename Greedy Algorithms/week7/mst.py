"""
Minimum Spanning Trees
-clustering
-networking
"""

"""
Prims Algorithm
Input: Undirected graph G= (V,E) and cost for edge (can be negative)
Output: MST - has all verticies and paths, no loops, minimal weights

- O(m logn) with heap, n^2 with min cycle
Steps:
- Start a random v
- for each unxplored v get min edge.
- repeat



Prim()
    S = new empty set
    for i = 1 to n
        d[i] = inf
    while S.size() < n
        x = inf
        v = -1
        for each i in V - S // V is the set of vertices
            if x >= d[v]
                then x = d[v], v = i
        d[v] = 0
        S.insert(v)
        for each u in adj[v]
            do d[u] = min(d[u], w(v,u))

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

def draw_graph(graph):
    """
    Function to visualise graph (adj list) with matplotlib
    """
    import networkx as nx
    import matplotlib
    import matplotlib.pyplot as plt

    G = nx.DiGraph(graph)
    nx.draw_networkx(G, with_labels = True, node_color = "c", edge_color = "k", font_size = 8, arrows=True)

    plt.axis('off')
    plt.draw()
    plt.show()

# draw_graph(graph)


def prim_iterative(graph):
    """
    Get MST from graph
    - Start a random v
    - for each unxplored v get min edge.
    - repeat
    """

    result = {v:{} for v in graph}
    unxeplored = {v for v in graph}
    explored = {unxeplored.pop()}

    while unxeplored:
        min_vertex = (float('inf'), None, None)
        for start in explored:
            for tail in graph[start]:
                #pick min tail
                if tail in unxeplored and graph[start][tail] < min_vertex[0]:
                    min_vertex = (graph[start][tail], start, tail)
        result[min_vertex[1]][min_vertex[2]] = min_vertex[0]
        explored.add(min_vertex[2])
        unxeplored.remove(min_vertex[2])
    total_weight = 0
    # from result graph calculate weight
    for v in result:
        for e in result[v]:
            total_weight += result[v][e]
    print("total", total_weight)

from heapq import heappush, heappop
def prim_queue(graph):
    """
    Get MST from graph
    - Start a random v
    - for each unxplored v get min edge.
    - repeat
    """
    queue = []
    result = {v:{} for v in graph}
    unxeplored = {v for v in graph}

    for start in graph:
        tail in graph[start]:
            heappush((graph[start][tail], start, tail))

    while queue:
        min_vertex = (float('inf'), None, None)
        for start in explored:
            for tail in graph[start]:
                #pick min tail
                if tail in unxeplored and graph[start][tail] < min_vertex[0]:
                    min_vertex = (graph[start][tail], start, tail)
        result[min_vertex[1]][min_vertex[2]] = min_vertex[0]
        explored.add(min_vertex[2])
        unxeplored.remove(min_vertex[2])
    total_weight = 0
    # from result graph calculate weight
    for v in result:
        for e in result[v]:
            total_weight += result[v][e]
    print("total", total_weight)


# prim_iterative(graph)

from collections import defaultdict

def test_quiz3(input):
    graph = defaultdict(dict)
    with open(input) as file:
        nodes, edges = file.readline().split()

        for line in file:
            start,end,weight = map(int, line.split())
            graph[start][end] = weight
            graph[end][start] = weight
    # draw_graph(graph)
    prim_iterative(graph)

test_quiz3("test_quiz3")
