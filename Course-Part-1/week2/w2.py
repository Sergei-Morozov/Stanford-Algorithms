import random

#pivot choose
def randomPivot(l,r):
    return random.randrange(l,r)
def firstPivot(A,l,r):
    return l
def lastPivot(A,l,r):
    return r-1
def medianPivot(A,l,r):
    m = l+((r-l)-1)/2
    slist= sorted([ (A[l],l), (A[r-1],r-1), (A[m],m)])
    median = slist[1]
    return median[1]

def partition(A,l,r):
    global TOTAL
    if r-l <= 1:
        return
    TOTAL += r-l -1

    p = partition.foo(A,l,r)
    pivot = A[p]
    A[l], A[p] = A[p], A[l]
    i = l + 1
    for j in range(i,r):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i +=1
    A[l], A[i-1] =A[i-1], A[l]
    partition(A, l, i-1)
    partition(A,i,r)

def quickSort( file , foo):
    global TOTAL
    TOTAL = 0
    A = []
    with open(file) as file:
        A = [int(line) for line in file]

    partition.foo = foo
    partition(A,0,len(A))
    assert(A == sorted(A))
    return TOTAL

print quickSort('input', firstPivot)
print quickSort('input', lastPivot)
print quickSort('input', medianPivot)

