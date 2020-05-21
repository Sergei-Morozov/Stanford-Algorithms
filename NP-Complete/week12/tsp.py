"""
Travelling salesman

input: complete undirected graph with nonnegative edge costs

output: a minimum cost tour that visit every vertex exactly once
"""

""" Build the graph
                  _____0____
                /     |    \
           10C /      |20C  \ 15C
             /  _____ 3____  \
            /  /25C     30C\  \
           1__/_____________\__2
                    35C
The minimum cost path is 0-1-3-2-0 = 10 + 25 + 30 + 15 = 80
"""
# a matrix representation of the graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


from itertools import permutations
def tsp_brute(graph):
    """
    - make all permutation of vertices O(N!)
    - for each permutation calculate path O(N)
    - return minimal O(1)
    Total is O(N*N!)
    """
    N = len(graph)
    paths = list(permutations(list(range(0,N)), N))

    minimum = float('inf')
    for path in paths:
        current  = 0
        # sum for each vertex in path
        for i in range(len(path)-1):
            current += graph[path[i]][path[i+1]]
        # add final edge tail -> start
        current += graph[path[-1]][path[0]]
        if minimum > current:
            minimum = current
    print(minimum)
    return minimum

# tsp_brute(graph)



N = len(graph)
memo = [ [-1 for _ in range(N)] for _ in range(1<<N)] # size [1 << N][N]
def tsp(bitmask, pos):
    """
    Let dp[bitmask][vertex] represent the minimum cost
        - bitmask 1 1 0 0  - represent visited vertex 3, 2 is equal 12
        - dp[12][2] - min cost for visited edges 3,2 and path ended in 2

    - number of possible sets = 2^(N-1) = 16777216
    - number of possible j = N-1 = 24
    - size of each element of A = 4 bytes = 32 bits (assuming float)
    """
    min_cost = float('inf')

    # All vertices have been explored 11111111
    if bitmask == ((1<<N) - 1):
        # cost to go back to 0 node
        return graph[pos][0]

    # if already computed
    if memo[bitmask][pos] != -1:
        return memo[bitmask][pos]

    # For every vertex
    for i in range(N):
        # If the vertex has not been visited
        if (bitmask & (1<<i)) == 0:
            min_cost = min(min_cost, tsp(bitmask | (1 << i) , i) + graph[pos][i])   # Visit the vertex

    memo[bitmask][pos] = min_cost
    return min_cost


print(tsp(1, 0))

from collections import defaultdict
from math import sqrt
def get_distance(d1, d2):
    return sqrt( (d1[0] - d2[0])**2 + (d1[1] - d2[1])**2)

def test_quiz3(input):

    distances = defaultdict(dict)
    with open(input) as file:
        number = file.readline()

        for idx, line in enumerate(file):
            x, y = map(float, line.split())
            distances[idx] = (x,y)

    graph = [[get_distance(distances[i],distances[j]) for j in range(25)] for i in range(25)]
    return graph

graph = test_quiz3('quiz1')
print('graph')
N = len(graph)
print('memo', 1<<N)
memo = [ [-1 for _ in range(N)] for _ in range(1<<N)] # size [1 << N][N]
print('tsp')
print(tsp(1, 0))













