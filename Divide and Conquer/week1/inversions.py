"""
Count inversions in given array
-Brute force
-Reccursion
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


