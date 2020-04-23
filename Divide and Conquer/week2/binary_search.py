"""
Binary search in sorted array
1. Split in 2 parts
2. Compare with middle point
3. Repeat
"""



def binary_search(x, input):
    """
    Search for value in array using slice
    """
    n = len(input)
    if n == 0 :
        return False
    if n == 1 and input[0] != x:
        return False

    mid_point = input[n//2]
    if x == mid_point:
        return True
    if x < mid_point:
        return binary_search(x, input[:n//2])
    if x > mid_point:
        return binary_search(x, input[n//2:])

def test_search(search):
    """
    Takes function to test search
    """
    input = [1, 2, 3, 8, 40, 99, 202, 220]

    for item in range(300):
        if item in input:
            assert search(item, input)
        else:
            assert not search(item, input)

test_search(binary_search)


def binary_search_index(x, input, low, high):
    """
    Search for value in array using index
    """
    if high < low :
        return False

    if high == low and input[low] != x:
        return False

    mid = (high+low)//2
    mid_point = input[mid]
    if x == mid_point:
        return True
    if x < mid_point:
        return binary_search_index(x, input, low, mid)
    if x > mid_point:
        return binary_search_index(x, input, mid+1, high)

def test_index_search(search):
    """
    Takes function to test search
    """
    input = [1, 2, 3, 8, 40, 99, 202, 220]

    for item in range(300):
        if item in input:
            assert search(item, input, 0, len(input)-1)
        else:
            assert not search(item, input, 0, len(input)-1)

test_index_search(binary_search_index)


def binary_search_iterative(x, input):
    """
    Binary search without recursion
    """
    low = 0
    high = len(input) - 1

    while high >= low:
        mid = (high+low) //2
        if x > input[mid]:
            low = mid + 1
        if x < input[mid]:
            high = mid -1
        if x == input[mid]:
            return True
    return False

test_search(binary_search_iterative)
