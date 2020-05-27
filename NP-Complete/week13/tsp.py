"""
Approximation on tsp
"""

from collections import defaultdict
from math import sqrt

def get_distance(d1, d2):
    return sqrt((d1[0] - d2[0])**2 + (d1[1] - d2[1])**2)

def get_x_distance(d1, d2):
    return d1[0] - d2[0]

def tsp(distances):
    """
    start at 0, build path to end, add final to start
    """
    explored = set([1])
    start = 1
    head = 1

    result = []
    path = [1]

    while len(explored) != len(distances):
        min_dist = float('inf')
        min_city = None
        for city in distances:
            if city not in explored:
                if min_dist > get_x_distance(distances[head], distances[city]):
                    distance = get_distance(distances[head], distances[city])
                    if min_dist > distance:
                        min_dist = distance
                        min_city = city
        result.append(min_dist)
        path.append(min_city)
        explored.add(min_city)
        head = min_city

    # add final step
    result.append(get_distance(distances[start], distances[head]))
    print(path)
    return result



def test_quiz(input):
    distances = defaultdict(dict)
    with open(input) as file:
        number = int(file.readline())

        for line in file:
            idx, x, y = map(float, line.split())
            distances[int(idx)] = (x,y)
    result = tsp(distances)
    print(sum(result))

test_quiz("quiz1")
