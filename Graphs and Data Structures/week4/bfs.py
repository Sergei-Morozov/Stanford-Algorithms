"""
BFS
- explore nodes in layers
- based on FIFO
- gives shortest path
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


def bsf_search(graph, start):
    """
    1. mark start explored (put in FIFO)
    2. while queue
       - get 1st element from queue
       - check unxeplored edges tails
       - put unxeplored tails to end of queue
       - put unxeplored tails destinace (previous + 1)
    """
    que = queue.Queue()
    que.put(start)

    #distance dict
    explored = {start: 0}

    while not que.empty():
        vertex = que.get()
        for tail in graph[vertex]:
            if tail not in explored:
                explored[tail] = explored[vertex] + 1
                que.put(tail)
    return explored

print(bsf_search(graph, 0))

"""
extra component to input graph
8 --- 9
"""
graph[8] = [9]
graph[9] = [8]

def connected_components(graph):
    """
    Find number of connected components in graph using BFS
    """
    explored = []
    components = 0
    for v in graph:
        if v not in explored:
            components += 1
            for v in bsf_search(graph, v):
                explored.append(v)
    return components


print(connected_components(graph))
