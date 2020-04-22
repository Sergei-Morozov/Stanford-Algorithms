"""
Question 1:
Download the text file here. (Right click and save link as)
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.
You can make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)
"""

with open("intArray.txt") as file:
    input = [int(line) for line in file]


def merge_split(left, right):
    """
    split 2 arrays in 1 sorted
    """
    idx_l = 0
    idx_r = 0
    result = []
    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] <= right[idx_r]:
            result.append(left[idx_l])
            idx_l += 1
        else:
            result.append(right[idx_r])
            idx_r += 1
    while idx_l < len(left):
        result.append(left[idx_l])
        idx_l += 1
    while idx_r < len(right):
        result.append(right[idx_r])
        idx_r += 1
    return result

def merge_sort(input):
    """
    1. divide
    2. merge_split
    """
    n = len(input)
    if n <= 1:
        return input
    left = merge_sort(input[:n//2])
    right = merge_sort(input[n//2:])
    split = merge_split(left,right)
    return split


sorted = merge_sort(input)
print(sorted)
