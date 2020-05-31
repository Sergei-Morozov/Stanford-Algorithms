"""
Input: directed weighted graph, weight is edge capacity(max it can flow)

Output: Max flow from s to t (multiple path)
"""



"""
    - > 1 ------> 3 -----|
    |   ^      /  ^      v
    0   ||   /    |      5
    |    v  v     |      ^
    - > 2 -------> 4 ----|
"""

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

def brute_bfs(graph, flow, s, t):
    """
    bfs from s to t, but f(e) < C(e)
    """
    distance = {k: [] for k in range(len(graph))}

    explored = set()
    que = queue.Queue()

    que.put(s)
    distance[s] = [s]

    while not que.empty():
        vertex = que.get()
        explored.add(vertex)
        for tail, capacity in enumerate(graph[vertex]):
            if capacity > flow[vertex][tail] and tail not in explored:
                que.put(tail)
                distance[tail] = distance[vertex] + [tail]
                if tail == t:
                    return distance[tail]

import queue

def max_flow(graph, s, t):
    """
    Greedy
    - Start with initial flow as 0.
    - bfs from s to t, but f(e) < C(e)
        - flow is capacity of min edge
        - update edges capacity
        - update max_flow with flow
        - repeat
    - return if no path
    """
    max_flow = 0
    flow = [[0 for _ in graph] for _ in graph]

    # BFS
    path = brute_bfs(graph, flow, s, t)

    while path:
        # get available flow
        min_flow = float('inf')
        for idx in range(1, len(path)):
            start = path[idx-1]
            end = path[idx]

            edge_capacity = graph[start][end] - flow[start][end]
            if edge_capacity < min_flow:
                min_flow = edge_capacity
        # reserve flow
        for idx in range(1, len(path)):
            start = path[idx-1]
            end = path[idx]
            flow[start][end] += min_flow

        # update max_flow
        max_flow +=min_flow

        #new path
        path = brute_bfs(graph, flow, s, t)

    return max_flow

print(max_flow(graph, 0, 5))


