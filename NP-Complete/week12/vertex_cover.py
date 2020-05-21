"""

Input: undirected graph G=(V,E)

Goal: minimum cardinality vertex cover
    (subset S that contains at least one endpoint of each edge of G)

"""

"""
INPUT graph and weights
 ---->1--->
|          |
0          2
|          |
 ---->3--->

"""

graph = {
    0: {1, 3},
    1: {0, 2},
    2: {1, 3},
    3: {0, 2},
}

def drop_vertex(graph, vertex):
    new_graph = {head:{tail for tail in edges if tail != vertex} for head, edges in graph.items() if head != vertex and edges != {vertex}}
    return new_graph

def vertex_cover(graph, k):
    """
    G(V,E) has cover of size k iif G'(V-u,E) or G''(V-v,E) has cover k-1

    1. pick edge (u,v)
    2. search for Gu for k-1
    3. search for Gv for k-1
    4. append S and U or V if found
    """
    if len(graph) == 0 and k == 0:
        return True
    for head in graph:
        for tail in graph:
            # try without head
            if vertex_cover(drop_vertex(graph, head), k-1):
                return True
            #try without tail
            if vertex_cover(drop_vertex(graph, tail), k-1):
                return True
    return False

print(vertex_cover(graph, 2))

"""
INPUT graph and weights


1-3---2
 /| \
4 5  6

"""

graph = {
    1: {3},
    2: {3},
    3: {1,2,3,4,5,6},
    4: {3},
    5: {3},
    6: {3},
}

print(vertex_cover(graph, 1))

