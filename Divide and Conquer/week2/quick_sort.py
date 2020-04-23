"""
Quick sort
1. Choose pivot point, swap with 0 elemnt
2. Swap values arround pivot in 2 areas: less and bigger
3. Swap pivot value from low to position between less|pivot|bigger
4. Recursively sort less and bigger parts
"""
import random

def swap(array, x, y):
    """
    swap inplace two values in given array
    """
    if x == y:
        return array
    array[x],array[y] = array[y],array[x]
    return array

def quickSort(array, low, high):
    """
    Quick sort on input array, pivot chosed uniformaly random
    """
    #base case
    if high - low <= 1:
        return array

    #randomly chosen pivot point to low position
    idx_pivot = random.randrange(low, high)
    swap(array, low, idx_pivot)

    pivot_value = array[low]
    idx_next = low + 1
    for i in range(low + 1, high):
        if array[i] < pivot_value:
            swap(array, idx_next, i)
            idx_next += 1


    #move pivot to correct position
    swap(array, low, idx_next-1)

    #recursion step
    quickSort(array, low, idx_next)
    quickSort(array, idx_next, high)
    return array


def test_qsort(function):
    input = [random.randrange(0, 10000) for _ in range(100)]
    assert sorted(input) == function(input, 0, 100)

test_qsort(quickSort)
