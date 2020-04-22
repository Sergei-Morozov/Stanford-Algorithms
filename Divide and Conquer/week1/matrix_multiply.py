"""
matrix multiplication  |a b| |e f| = |ae+bg af+bh|
                       |c d| |g h|   |ce+dg cf+dh|

Zij = E(k->n) Xik * Ykj
ith row of X on  vth column of Y
"""

x = [
    [1, 2],
    [3, 4]
    ]

y = [
    [5, 6],
    [7, 8]
    ]


def brute_multiply_matrix(x, y):
    """
    Zij = sum(Xik * Ykj)
    """
    rows = len(x)
    columns = len(x[0])

    result = [[0 for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            result[row][column] = x[row][0] * y[0][column] + x[row][1] * y[1][column]
    return result

result = brute_multiply_matrix(x,y)

def strassen_multiply_matrix(x,y):
    """
    Strassen algortim
    for matrix multiplication
    compute 7 products of elements - use them with formula

    matrix multiplication  |a b| |e f| = |P5+P4-P2+P6  P1+P2.     | = |ae+bg af+bh|
                           |c d| |g h|   |P3+P4        P1+P5-P3-P7|   |ce+dg cf+dh|
    """
    pass

