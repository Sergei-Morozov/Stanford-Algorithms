"""
DFS
- explore full paths aggressively
- based on LIFO (stack) or recursion
- can be used for Topological order sort
"""
import queue
"""
INPUT:
0 --- 1 ---2 --- 3
|  /  |    |  /  |
4 --- 5 ---6 --- 7

"""

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

def dfs(graph, start):
    """
    Iterative realisation using stack (LIFO)
    """
    que = queue.LifoQueue()
    que.put(start)
    explored = [start]

    while not que.empty():
        vertex = que.get()
        for tail in graph[vertex]:
            if tail not in explored:
                explored.append(tail)
                que.put(tail)
    return explored

print(dfs(graph,0))

def dfs_recurisive(graph, start, explored):
    """
    Recursive realization of DFS
    """
    explored.append(start)
    for tail in graph[start]:
        if tail not in explored:
            dfs_recurisive(graph, tail, explored)
    return explored

print(dfs_recurisive(graph, 0, []))


"""
   -> 2
1       ->4
   -> 3
"""

directed_graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [],
}

def dfs_ordered(graph, start, explored, result, n):
    explored.append(start)
    for tail in graph[start]:
        if tail not in explored:
            n = dfs_ordered(graph, tail, explored, result, n)
    result[start] = n
    return n-1


def topological_sort(graph):
    """
    Topologically sort graph with DFS
    Assign labels for each u,v such that label(u) < f(v) if there edge u,v
    """
    result = {}
    explored = []
    n = len(graph)

    for v in graph:
        if v not in explored:
            n = dfs_ordered(graph, v, explored, result, n)
    return result

print(topological_sort(directed_graph))

