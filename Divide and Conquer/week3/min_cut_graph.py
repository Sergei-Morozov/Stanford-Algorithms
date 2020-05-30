"""
Minimal cut graph
1. Until remain 2 vertices
2. Pick uniformally random edge
3. Merge head-tail in single V, remove self-loops
"""
import random
"""
INPUT:
0 --- 1 ---2 --- 3
|  /  |    |  /  |
4 --- 5 ---6 --- 7

"""

def draw_graph(graph):
    """
    Function to visualise graph (adj list) with matplotlib
    """
    import networkx as nx
    import matplotlib
    import matplotlib.pyplot as plt

    G = nx.Graph(graph)
    nx.draw_networkx(G, with_labels = True, node_color = "c", edge_color = "k", font_size = 8)

    plt.axis('off')
    plt.draw()
    plt.show()

graph = {
    0: [1,4],
    1: [0,2,4,5],
    2: [1,3,6],
    3: [2,6,7],
    4: [0,1,5],
    5: [1,4,6],
    6: [2,3,5,7],
    7: [3,6],
}

def minimal_cut(graph):
    """
    Cut graph in 2 parts
    """
    #base case
    vertices = list(graph.keys())
    if len(vertices) == 2:
        return graph

    #pick random edge
    h = random.choice(vertices)
    t = random.choice(graph[h])
    print(f"Head: {h}, Tail: {t}")

    #merge head & tail in one
    for e in graph[t]:
        # edges from tail add to head
        graph[h].append(e)
        # add references to other about head
        graph[e].append(h)
        # remove tail references from others
        graph[e].remove(t)

    #remove tail
    graph.pop(t)

    #remove self loops
    graph[h] = [e for e in graph[h] if e!=h]

    #recursion
    return minimal_cut(graph)



#Run this V^2 times to get best cut
min_cut = float('inf')
min_graph = None
for _ in range(7**2):
    from copy import deepcopy
    cut = minimal_cut(deepcopy(graph))
    size = len(cut[list(cut.keys())[0]])
    if size < min_cut:
        min_graph = cut
        min_cut = size

#Minimal cut
print(min_cut)
draw_graph(min_graph)


















