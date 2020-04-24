"""
Randomized Select of ith sorted value
1 select pviot
2 arrange values, move pivot to correct position
3 compare with ith, recursively search second part
"""
import random
def swap(array, x, y):
    """
    swap 2 indexes in array
    """
    if x != y:
        array[x], array[y] = array[y], array[x]


def rselect(array, ith, low, high):
    """
    Return ith element from sorted array
    """
    if (high - low) == 1:
        return array[low]

    pivot_idx = random.randrange(low, high)

    # move pivot to low
    swap(array, low, pivot_idx)

    idx_less = low + 1
    pivot_value = array[low]
    for i in range(low+1, high):
        if array[i] < pivot_value:
            swap(array, i, idx_less)
            idx_less += 1

    # move pivot to correct position
    pivot_idx = idx_less - 1
    swap(array, low, pivot_idx)
    if pivot_idx == ith:
        return array[ith]
    elif ith < pivot_idx:
        return rselect(array, ith, low, pivot_idx)
    elif ith > pivot_idx:
        return rselect(array, ith, pivot_idx+1, high)

input = [1, 2, 3, 5, 4]

result = rselect(input, 4, 0, len(input))
print(result)
