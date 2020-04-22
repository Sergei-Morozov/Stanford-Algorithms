"""
Closest pair from 2 arrays of distinct points
where distance = sqrt((x-x)^2 + (y-y)^2)
1)We sort all points according to x coordinates.
2)Divide all points in two halves.
3)Recursively find the smallest distances in both subarrays.
4)Take the minimum of two smallest distances. Let the minimum be d.
5)Create an array strip[] that stores all points which are at most d distance away from the middle line dividing the two sets.
6)Find the smallest distance in strip[].
7)Return the minimum of d and the smallest distance calculated in above step 6.

"""
from math import sqrt

def distance(p1, p2):
    """
    distance between 2 points sqrt((x-x)^2 + (y-y)^2)
    """
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

points = [(1,2), (0,9), (5,6), (10,4), (0,1), (20, 4)]

def brute_closest_pair(points):
    """
    Find closest pair of point in array using brute force
    """
    n = len(points)
    min_distance = float("inf")
    last_pair = None
    for i in range(n):
        for j in range(i+1, n):
            result = distance(points[i], points[j])
            if result < min_distance:
                min_distance = result
                last_pair = [points[i], points[j]]
    return last_pair

def best_pair(p1,p2,p3):
    """
    Calculate distance in pair, return best
    """
    left_distance = float("inf")
    right_distance = float("inf")
    split_distance = float("inf")
    if p1:
        left_distance = distance(p1[0], p1[1])
    if p2:
        right_distance = distance(p2[0], p2[1])
    if p3:
        split_distance = distance(p3[0], p3[1])

    min_distance = min(left_distance, right_distance, split_distance)
    if min_distance == left_distance:
        return p1
    elif min_distance == right_distance:
        return p2
    else:
        return p3

def closest_split_pair(x, delta):
    """
    Get mid point, seek for point +/- delta from mid point
    should 7 points away in y
    """
    mid_point_x = x[len(x)//2][0]
    strip = []

    for point in y:
        if abs(mid_point_x - point[0]) < delta:
            strip.append(point)
    strip = sorted(strip, key= lambda x: x[0])

    n = len(strip)
    min_distance = float("inf")
    last_pair = None
    for i in range(n):
        for j in range(i+1, i+7):
            if j < n:
                result = distance(points[i], points[j])
                if result < min_distance:
                    min_distance = result
                    last_pair = [points[i], points[j]]
    return last_pair

def closest_pair(x):
    """
    assume array was already sorted
    """
    n = len(x)
    if n <= 2:
        return brute_closest_pair(x)
    left_pair = closest_pair(x[:n//2])
    right_pair = closest_pair(x[n//2:])
    delta = distance(*best_pair(left_pair, right_pair, None))
    split_pair = closest_split_pair(x, delta)

    return best_pair(left_pair, right_pair, split_pair)


print("closest brute pair")
result = brute_closest_pair(points)
print(result)

print("closest d&q pair")
px = sorted(points, key= lambda x: x[0])
result = closest_pair(px)
print(result)
