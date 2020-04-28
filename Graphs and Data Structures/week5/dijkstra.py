"""
Dijkstra's shortest path
(Imp: all edges has nonnegative length)

- BFS with weights
- On each iteration
- add to dict
-
"""


"""
INPUT graph and weights
 ---->1--->
| 2     1 |
0         2
| 3     2 |
 ---->3--->

"""

graph = {
    0: {1:2, 3:3},
    1: {2:1},
    2: {},
    3: {2:2},
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


def dijkstra_list(graph, start):
    """
    Use list to find min distances
    """
    distances = {start:0}
    vertex2explore = set([vertex for vertex in graph])

    while vertex2explore:
        min_vertex = None
        for vertex in vertex2explore:

            #find minimal vertex distance in not explored
            if vertex in distances:
                if min_vertex is None:
                    min_vertex = vertex
                elif distances[vertex] < distances[min_vertex]:
                    min_vertex = vertex

        if min_vertex is None:
            break

        vertex2explore.remove(min_vertex)

        # update distances
        for tail in graph[min_vertex]:
            if tail in vertex2explore:
                distance2tail = distances[min_vertex] + graph[min_vertex][tail]
                if distances.get(tail, float('inf')) > distance2tail:
                    distances[tail] = distance2tail
    return distances

import heapq
def dijkstra_heap(graph, start):
    """
    Use heap structure to get min vertex fast, instead iteration over list
    """
    distances = {}
    explored = set()

    heap = [(0, start)]
    while heap:
        # get next step min distance vertex and add to explored
        distance, min_vertex = heapq.heappop(heap)
        distances[min_vertex] = distance
        explored.add(min_vertex)

        # For E tail not yet explored update values if less
        for tail in graph[min_vertex]:
            if tail not in explored:
                distance2tail = distance + graph[min_vertex][tail]
                if distances.get(tail, float('inf')) > distance2tail:
                    heapq.heappush(heap, (distance2tail, tail))
    return distances






print(dijkstra_list(graph, 0))

print(dijkstra_heap(graph, 0))

# draw_graph(graph)

