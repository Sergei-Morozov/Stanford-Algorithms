"""
Johnson base on reweighting negative edges
- 1 invocation bellman ford
- n invocations of Dijkstra

Reweighting every negative edge  c'(u,w) = c(u,w) + p(u) - p(v)
    where p(u) and p(v)

- add artificial vertex S connected to all v in graph with zero length
- invoke bellman-ford get p(v) table and update weights
-
"""

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

        if min_vertex not in explored:
            distances[min_vertex] = distance
            explored.add(min_vertex)

            # For E tail not yet explored update values
            for tail in graph[min_vertex]:
                if tail not in explored:
                    distance2tail = distance + graph[min_vertex][tail]
                    if distances.get(tail, float('inf')) > distance2tail:
                        distances[tail] = distance2tail
                        heapq.heappush(heap, (distance2tail, tail))
    return distances

from bellman_ford import bellman_ford


def johnson(graph):
    """
    1. Add new Vertex with 0 weight edge to all vertex
    2. Run bellman ford
    3. update edge weights
    4. run dijkstra for each v
    5. update final result with weights
    """

    graph[-1] = {k:0 for k in graph}

    weights = bellman_ford(graph, -1)

    graph.pop(-1)
    for head in graph:
        for tail in graph[head]:
            graph[head][tail] = graph[head][tail] + weights[head] - weights[tail]

    final_weights = []
    for u in graph:
        distances = dijkstra_heap(graph, u)
        for v in distances:
            distances[v] = distances[v] - weights[u] + weights[v]
        final_weights.append(distances)

    # print(final_weights)
    print(min([min([item[v] for v in item]) for item in final_weights]))

from collections import defaultdict
def test_quiz3(input):
    graph = defaultdict(dict)
    with open(input) as file:
        nodes, edges = file.readline().split()

        for line in file:
            start,end,weight = map(int, line.split())
            graph[start][end] = weight
    johnson(graph)

if __name__ == '__main__':
    g = []

    g = {
        0: {1: -1, 2: 4},
        1: {2:3, 3:2, 4: 2},
        2: {},
        3: {2:5, 1:1},
        4: {3:-3},
    }

    # draw_graph(g)
    result = johnson(g)
    test_quiz3('quiz3')
