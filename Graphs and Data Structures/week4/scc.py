"""
Determine strongly connected components (DFS)
Kosaraju Two-Pass algorithm
- make G(reversed) = G with all arcs reversed
- run DFS-loop on G(reversed) to get ranking
- run DFS-loop on G using ranking from previous step
"""

def reverse_graph(graph):
    """
    Reverse all graph arcs
    """
    new_graph = {k: [] for k in range(1, len(graph)+1)}
    for head in graph:
        for tail in graph[head]:
            new_graph[tail].append(head)
    return new_graph


def dfs(graph, explored, start, ranks, n):
    """
    Run DFS using
    - explored set
    - start vertex
    - result rankings
    - n weigth value
    """
    explored.add(start)
    for tail in graph[start]:
        if tail not in explored:
            n = dfs(graph, explored, tail, ranks, n)
    ranks[n] = start
    return n + 1

def dfs_loop(graph, vertex_order):
    """
    Calculate topological orders on graph
    Relies on vertex order [0, ..., n]
    """
    ranking = {}
    explored = set()
    n = 1

    # logic to print resulted components at the end
    last = 0
    components = []

    for vertex in vertex_order:
        if vertex not in explored:
            n = dfs(graph, explored, vertex, ranking, n)

            #related to print
            components.append(len(explored) - last)
            last = len(explored)

    # print 5 largest components for quiz
    print(sorted(components, reverse=True)[:5])
    return ranking

def test():
    """
    It has 3 components
    1 ---> 2   ---- 4 --- 5 --- 8 -- 9
    ^               |     |       \  |
    |  /            6 <-  7          10
    3

    """
    graph = {
        1: [2],
        2: [4,3],
        3: [1],
        4: [5],
        5: [7,8],
        6: [4],
        7: [6],
        8: [9],
        9: [10],
        10: [8],
    }

    #get reversed graph
    r_graph = reverse_graph(graph)
    #test input order
    order = [7,2,1,4,5,6,3,8,9,10]
    #compute ranking
    ranking = dfs_loop(r_graph, order)
    #make new order of vertices
    new_order = [ranking[k] for k in range(10, 0, -1)]

    # finally get SCC properties of original graph
    dfs_loop(graph, new_order)


def quiz():
    """
    Solve quiz for week 4
    """
    graph = {i:[] for i in range(1, 875715)}
    order = [k for k in range(875714, 0, -1)]

    # parse input data to adj list
    with open("scc-input") as input:
        for edge in input:
            head, tail = edge.split()
            graph[int(head)].append(int(tail))

    #reversed graph
    r_graph = reverse_graph(graph)
    ranking = dfs_loop(r_graph, order)
    new_order = [ranking[k] for k in range(875714, 0, -1)]

    #finally get SCC properties of original graph
    dfs_loop(graph, new_order)


# quiz is too large to handle, set sys and threading
import sys
sys.setrecursionlimit(800000)
import threading
threading.stack_size(67108864)
thread = threading.Thread(target=quiz)
thread.start()

