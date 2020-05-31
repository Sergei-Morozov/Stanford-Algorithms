"""
Refer to week4

Determine strongly connected components (DFS)
Kosaraju Two-Pass algorithm
- make G(reversed) = G with all arcs reversed
- run DFS-loop on G(reversed) to get finish ranking
- run DFS-loop on G using ranking from previous step

Based:
C1 -> C2  - scc componets in original G
C1 <- C2 - scc in reversed , so C2 rank always bigger ten C1 rank
starting in C2 will reveal C2 connected vertices
"""

def reversed_graph(graph):
    """
    make head->tail == tail -> head
    """
    r_graph = {k:[] for k in graph}

    for head in graph:
        for tail in graph[head]:
            r_graph[tail].append(head)
    return r_graph

def scc_dfs(graph, vertex, explored, stack):

    explored.add(vertex)
    for tail in graph[vertex]:
        if tail not in explored:
            scc_dfs(graph, tail, explored, stack)
    stack.append(vertex)

def get_scc_order(graph, order):
    """
    Compute new order based on graph/order using dfs
    """
    explored = set()
    stack = []

    for vertex in order:
        if vertex not in explored:
            scc_dfs(graph, vertex, explored, stack)
    return stack

def get_scc_components(graph, new_order):
    """
    explore dfs in order
    """
    explored = set()
    result = []
    for vertex in new_order[::-1]:
        if vertex not in explored:
            component = []
            scc_dfs(graph, vertex, explored, component)
            result.append(component)
    return result

def scc(graph):
    """
    - make G(reversed)
    - run DFS-loop on G(reversed) to get finish ranking
    - run DFS-loop on G using ranking from previous step to reveal SCC
    """
    r_graph = reversed_graph(graph)

    # random order vertices
    order = [k for k in graph]
    # get new order
    new_order = get_scc_order(graph, order)
    # run with new ranks on original
    components = get_scc_components(r_graph, new_order)

    return components


def test1():
    """
    It has 3 components
    1 ---> 0   ----> 3
    ^     /         |
                    v
    |  /            4
      v
    2

    """
    graph = {
        0: [3,2],
        1: [0],
        2: [1],
        3: [4],
        4: [],
    }

    components = scc(graph)
    print(components)

def test2():
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

    components = scc(graph)
    print(components)

