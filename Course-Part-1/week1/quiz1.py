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
