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

def prim_dict(graph):
    """
    Get MST from graph (same as Dijkstra but distance are just edge weights)
    - Start a random v
    - for each unxplored v get min distnce.
    - repeat
    """
    distances = dict()
    unxeplored  = {v for v in graph}

    #update start point
    vertex = unxeplored.pop()
    distances[vertex] = 0
    for tail in graph[vertex]:
        distances[tail] = graph[vertex][tail]

    while unxeplored:
        min_vertex = None
        for vertex in unxeplored:
            if vertex in distances:
                if distances.get(min_vertex, float('inf')) > distances[vertex]:
                    min_vertex = vertex
        unxeplored.remove(min_vertex)

        for tail in graph[min_vertex]:
            if tail in unxeplored:
                if distances.get(tail, float('inf')) > graph[min_vertex][tail]:
                    distances[tail] = graph[min_vertex][tail]

    total_weight = 0
    # from result graph calculate weight
    for v in distances:
        total_weight += distances[v]
    print("total", total_weight)

from heapq import heappush, heappop
def prim_heap(graph):
    """
    Use Heap to get min distance same as dict
    """
    distances = dict()
    explored = set()

    # start with ~random~ vertex
    heap =[(0, 1)]

    while heap:
        min_distance, min_vertex = heappop(heap)
        if min_vertex not in explored:
            explored.add(min_vertex)
            distances[min_vertex] = min_distance

            # update tails
            for tail in graph[min_vertex]:
                if tail not in explored:
                    heappush(heap, (graph[min_vertex][tail], tail))

    # from result graph calculate weight
    total_weight = 0
    for v in distances:
        total_weight += distances[v]
    print("total", total_weight)
    return distances

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
    prim_dict(graph)
    prim_heap(graph)
test_quiz3("quiz3")
