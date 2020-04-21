"""
Count inversions in given array
-Brute force
-Recursion
"""

array = [1, 3, 5, 2, 4, 6]

def brute_count_inversion(array):
    num = 0
    for i in range(len(array)):
        for j in range(i + 1):
            if array[i] < array[j]:
                num += 1
    return num


def merge(left, right, n):
    """
    Merge step of MergeSort
    """
    result = []
    idx_right = 0
    idx_left = 0
    inversion = 0
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] <= right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1
            inversion += len(left) - idx_left

    if idx_left < len(left):
        result.extend(left[idx_left:])
    if idx_right < len(right):
        result.extend(right[idx_right:])

    return result, inversion


def count_inversion(array):
    # recursion base case
    n = len(array)
    if n == 0:
        return [], 0
    if n == 1:
        return array, 0

    left, left_inverted = count_inversion(array[:int(n // 2)])
    right, right_inverted = count_inversion(array[int(n // 2):])
    result, merge_inversions = merge(left, right, n)

    return result, left_inverted + right_inverted + merge_inversions


inversion = brute_count_inversion(array)
print(inversion)

result, inversions = count_inversion(array)
print(inversion)
print(result)



"""
matrix multiplication  |a b| |e f| = |ae+bg af+bh|
                       |c d| |g h|   |ce+dg cf+dh|

Zij = E(k->n) Xik * Ykj
ith row of X on  vth column of Y
"""

x = [
    [1, 2],
    [3, 4]
    ]

y = [
    [5, 6],
    [7, 8]
    ]


def brute_multiply_matrix(x, y):
    """
    Zij = sum(Xik * Ykj)
    """
    rows = len(x)
    columns = len(x[0])

    result = [[0 for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            result[row][column] = x[row][0] * y[0][column] + x[row][1] * y[1][column]
    return result

result = brute_multiply_matrix(x,y)

def strassen_multiply_matrix(x,y):
    """
    Strassen algortim
    for matrix multiplication
    compute 7 products of elements - use them with formula

    matrix multiplication  |a b| |e f| = |P5+P4-P2+P6  P1+P2.     | = |ae+bg af+bh|
                           |c d| |g h|   |P3+P4        P1+P5-P3-P7|   |ce+dg cf+dh|
    """
    pass


"""
Closest pair from 2 arrays of distinct points
where distance = sqrt((x-x)^2 + (y-y)^2)
1. Px sort by x
2. Py sort by y
3. split to n/2 (Qx, Qy, Rx, Ry)
4. get best points for n/2
5. get best distance between these n/2 points
6. pass best distance to split Px Py

"""
from math import sqrt

def distance(p1, p2):
    """
    distance between 2 points sqrt((x-x)^2 + (y-y)^2)
    """
    if len(p1) == 0 or len(p2) == 0:
        return 0
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

points = [(1,2), (0,9), (5,6), (10,4)]

def brute_closest_pair(points):
    """
    Find closest pair of point in array using brute force
    """
    n = len(points)
    max_distance = 0
    last_pair = None
    for i in range(n):
        for j in range(i, n):
            result = distance(points[i], points[j])
            if result > max_distance:
                max_distance = result
                last_pair = [points[i], points[j]]
    return last_pair





px = sorted(points, key= lambda x: x[0])
py = sorted(points, key= lambda x: x[1])

def closest_split_pair(x, y, distance):
    pass

def best_pair(p1,p2,p3):
    """
    Calculate distance in pair, return best
    """
    left_distance = distance(p1[0], p1[1])
    right_distance = distance(p2[0], p2[1])
    split_distance = distance(p3[0], p3[1])
    min_distance = min(left_distance, right_distance, split_distance)
    if min_distance == left_distance:
        return p1
    elif min_distance == right_distance:
        return p2
    else:
        return p3

def closest_pair(x, y):
    """
    assume array was already sorted
    """
    n = len(x)
    left_pair = closest_pair(x[:n//2], y[:n//2])
    right_pair = closest_pair(x[n//2:], y[n//2:])
    delta = min(distance(left_pair[0], left_pair[1]), distance(right_pair[0], right_pair[1]))
    split_pair = closest_split_pair(x, y, delta)

    return best_pair(left_pair, right_pair, split_pair)




#11.180339887498949
# result = closest_pair(px, py)
# print(result)

