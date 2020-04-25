"""
Determenistic select ith order value from unsroted array
Works exactly in O(n)=n time using median of median
1. Get n/5 splits from original array ans sort them
2. From n/5 arrays get their median elements and then select its n/10 (it will be bigger then 3n/10 elements)
3. Use this as pivot, move to right position, procced with left or right part recursivelly
"""
def swap(array, x, y):
    """
    Swap 2 idx in array
    """
    if x != y:
        array[x], array[y] = array[y], array[x]


def dselect(array, ith):
    """
    Determenistic select, choose pivot median of medain 30/70 split
    return ith sorted element
    """

    # assert ith is order of input array

    n = len(array)

    #base case, for small array compute median
    if n <= 5:
        return sorted(array)[ith]

    # get medians from all n/5 arrays
    medians = []
    for i in range(0, n, 5):
        part = sorted(array[i:i+5])
        medians.append(part[len(part)//2])

    # get n/10 (median of median) from medians array, find pos in original array
    # 1st recursive call
    pivot = dselect(medians, len(medians)//2)

    # split array in 2 parts
    less = [i for i in array if i < pivot]
    more = [i for i in array if i > pivot]

    # base cases
    # 1. ith == less +1
    # 2. ith in smaller part
    # 3. ith in remided bigger part (size n - less -pivot)
    if ith == len(less):
        return pivot
    if ith < len(less):
        return dselect(less, ith)
    elif ith > len(less):
        return dselect(more, ith - (len(less)+1))


# Run tests
def test_select(function):
    input = [i for i in range(0,100)]

    for i in range(0,100):
        assert input[function(input, i)] == i

test_select(dselect)

input = [2, 1, 3, 5, 4, 8, 6, 9, 7, 0]
print(dselect(input, 9))
