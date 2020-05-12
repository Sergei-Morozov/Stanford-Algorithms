"""
Sequence alingment (Needleman-Wunsch score, similiarity between 2 strings)

Input:
    - AGGGCY
    - AGGCA

Output:
    - AGGGCY   (x + gaps)
    - AGG-CA   (y + gaps)
    Mimized Total penalty = 1*gap + 1*replace

"""

gap_cost = 3
replace_cost = 7
def sequence_brute(str1, str2, x, y):
    """
    Cases:
        - equal
        - gap str1 <=> str2
        - replace
    """
    if x == 0 :
        return y * gap_cost
    if y == 0:
        return x * gap_cost

    if str1[x] == str2[y]:
        return sequence_brute(str1, str2, x-1, y-1)
    else:
        return min(
            gap_cost + sequence_brute(str1, str2, x-1, y),
            gap_cost + sequence_brute(str1, str2, x, y-1),
            replace_cost + sequence_brute(str1, str2, x-1, y-1)
            )


gap_cost = 3
replace_cost = 7
assert sequence_brute("-GC", "-CA", 2, 2) == 6


gap_cost = 3
replace_cost = 2
assert sequence_brute("-AGGGCT", "-AGGCA", 6, 5) == 5


gap_cost = 3
replace_cost = 5
assert sequence_brute("-CG", "-CA", 2, 2) == 5

def sequence(A, str1, str2, x, y):
    """
    DP using 2D array A[x][y]
    Cases:
        - equal
        - gap str1 <=> str2
        - replace
    """
    if A[x][y] != -1:
        return A[x][y]

    if x == 0 :
        return y * gap_cost
    if y == 0:
        return x * gap_cost

    if str1[x] == str2[y]:
        A[x][y] = sequence(A, str1, str2, x-1, y-1)
    else:
        A[x][y] = min(
            gap_cost + sequence(A, str1, str2, x-1, y),
            gap_cost + sequence(A, str1, str2, x, y-1),
            replace_cost + sequence(A, str1, str2, x-1, y-1)
            )
    return A[x][y]


gap_cost = 3
replace_cost = 7
A = [[ -1 for _ in range(3)] for _ in range(3)]
for i in range(3):
    A[i][0] = i*gap_cost
    A[0][i] = i*gap_cost
assert sequence(A, "-GC", "-CA", 2, 2) == 6


gap_cost = 3
replace_cost = 2
A = [[ -1 for _ in range(6)] for _ in range(7)]
for i in range(6):
    A[i][0] = i*gap_cost
for i in range(5):
    A[0][i] = i*gap_cost
assert sequence(A, "-AGGGCT", "-AGGCA", 6, 5) == 5


def sequence_iter(str1, str2, x, y):
    """
    DP using 2D array A[x][y]
    Cases:
        - equal
        - gap str1 <=> str2
        - replace
    """
    A = [[ None for _ in range(y+1)] for _ in range(x+1)]
    for i in range(x+1):
        A[i][0] = i*gap_cost
    for i in range(y+1):
        A[0][i] = i*gap_cost

    for x_idx in range(1, x+1):
        for y_idx in range(1, y+1):
            if str1[x_idx] == str2[y_idx]:
                A[x_idx][y_idx] = A[x_idx-1][y_idx-1]
            else:
                A[x_idx][y_idx] = min(
                    gap_cost + A[x_idx-1][y_idx],
                    gap_cost + A[x_idx][y_idx-1],
                    replace_cost + A[x_idx-1][y_idx-1]
                    )
    cost = A[x][y]

    print(A)
    x1 = x
    y2 = y
    result1 = ""
    result2 = ""

    while x >0 and y>0:
        #equal
        print(x,y)
        print(str1[x], str2[y])

        if A[x][y] == A[x-1][y-1]:
            print("equal")
            result1 = str1[x] + result1
            result2 = str2[y] + result2
            x -= 1
            y -= 1
        #compare
        elif A[x][y] == A[x-1][y-1] + replace_cost:
            print("cmp")

            result1 = str1[x] + result1
            result2 = str2[y] + result2
            x -= 1
            y -= 1
        # first gap
        elif A[x][y] == A[x-1][y] + gap_cost:
            print("1gap")

            result1 = '-' + result1
            result2 = str2[y] + result2
            x -= 1
        # second gap
        elif A[x][y] == A[x][y-1]  + gap_cost:
            print("2gap")

            result1 = str1[x] + result1
            result2 = '-' + result2
            y -= 1
        else:
            print('error')
            print(x, y)
            print(result1, result2)
            return
    while x > 0:
        result1 = str1[x] + result1
        x -= 1

    while y > 0:
        result2 = str2[y] + result2
        y -= 1
    print(result1, result2)

gap_cost = 3
replace_cost = 2
print(sequence_iter(" AGGGCT", " AGGCA", 6, 5)) #5
