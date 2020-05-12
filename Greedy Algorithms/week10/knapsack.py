"""
Knapsack

Input:
    n items
    - value vi
    - size wi
    - capacity x
Ouput:
    - subset of n that maximize value

Details:
    use - 2D array (items, capacity)
    A[0,x] = 0 for all x
    A[i,x] = max{A[i-1,x], A[i-1, x-wi] + vi}
                 exclude   included
            both can be previously computed

    - traceback to get set of items
"""
from dataclasses import dataclass

@dataclass
class Item:
    value: int
    size: int

def knapsack_recursive(values, weights, n, capacity):
    """
    Recursion all combination either include/exclude item
    """
    if n == 0 or capacity == 0:
        return 0

    # if weight of n item > capacity
    # cant include it
    if (weights[n-1] > capacity):
        return knapsack_recursive(values, weights, n-1, capacity)
    else:
        # max without or max with (value + knapsack(capacity - weight))
        return max(knapsack_recursive(values, weights, n-1, capacity), values[n-1] + knapsack_recursive(values, weights, n-1, capacity-weights[n-1]))

def knapsack_recursive_dp(array, values, weights, n, capacity):
    """
    Recursion all combination either include/exclude item
    """
    if n == 0 or capacity == 0:
        return 0
    if array[n][capacity] != None:
        return array[n][capacity]

    # if weight of n item > capacity
    # cant include it
    if (weights[n-1] > capacity):
        array[n][capacity] = knapsack_recursive(values, weights, n-1, capacity)
        return array[n][capacity]
    else:
        # max without or max with (value + knapsack(capacity - weight))
        array[n][capacity] = max(knapsack_recursive(values, weights, n-1, capacity), values[n-1] + knapsack_recursive(values, weights, n-1, capacity-weights[n-1]))
        return array[n][capacity]



def knapsack(values, weights, capacity):
    """
    use 2d array
    """
    n = len(values)
    saved = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for idx in range(n+1):
        for w in range(capacity+1):
            if idx ==0 or w == 0:
                saved[idx][w] = 0
            elif weights[idx-1] <= w:
                saved[idx][w] = max(saved[idx-1][w], saved[idx-1][w - weights[idx-1]] + values[idx-1])
            else:
                saved[idx][w] = saved[idx-1][w]
    return saved[n][capacity]


def knapsack_iterate_back(save):
    """
    Iterate 2D array backwards to get actual choice of items
    """
    pass


def test1():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    expected_answer = 220

    result = knapsack_recursive(values, weights, 3, capacity)
    assert result == expected_answer


    items = 3
    array = [[None for _ in range(capacity+1)] for _ in range(items+1)]
    for i in range(capacity+1):
        array[0][i] = 0
    for i in range(items+1):
        array[i][0] = 0

    print(knapsack_recursive_dp(array, values, weights, items, capacity))

    result = knapsack(values, weights, capacity)
    assert result == expected_answer

test1()



def test_quiz(input):
    with open(input) as file:
        capacity, items = map(int, file.readline().split())
        values = []
        weights = []
        for line in file:
            value, weight = map(int, line.split())
            values.append(value)
            weights.append(weight)
    print(knapsack(values, weights, capacity))

    array = [[None for _ in range(capacity+1)] for _ in range(items+1)]
    print(knapsack_recursive_dp(array, values, weights, items, capacity))


# test_quiz('quiz1')
# test_quiz('quiz2')
#2493893
#4243395


