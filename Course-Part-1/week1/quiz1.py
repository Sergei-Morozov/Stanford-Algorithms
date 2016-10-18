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
arr = []
with open('intArray.txt') as file:
    for line in file:
        arr.append(int(line))

print(len(arr))
#arr = [1, 6,3,2,4,5]
inversion = 0


def msort(arr):
    #print arr
    if len(arr) == 1:
        return arr
    mid = len(arr) / 2
    #print('mid', mid)
    a = msort(arr[:mid])
    b = msort(arr[mid:])
    return merge(a, b)


def merge(a, b):
    global inversion
    #print(a,b)
    la = len(a)
    lb = len(b)
    res = []
    j = 0
    k = 0
    while j < la and k < lb:
        if a[j] < b[k]  :
            res.append(a[j])
            j += 1
        else:
            inversion += la - j
            res.append(b[k])
            k += 1
    if j<la:
        res += [a[i] for i in range(j,la)]
    elif k < lb:
        res += [b[i] for i in range(k,lb)]
    return res

print( 'RESULT', msort(arr))
#print merge([1,1,1], [2,2,2])
print(inversion)
