"""
Dynamic programming
input: path graph  1---4---5---4
output: independent set of max total weight

Idea:
An optimal solution can have one of two properties:
- Either the last element in the path is not part of the maximum weighted independent set (in which case we know that the solution is equally valid for the subgraph V’ formed by popping the last vertex off the path)
- Or the last element is part of the set (in which case we know that the predecessor cannot be part of the set, and the solution minus the last vertex is equally valid for the subgraph V’’ formed by popping off the last two vertices of the path)


A[i] = max(A[i-1], A[i-2] +wi)
"""
def wis_iterative(input, n):
    """
    Brute force approach
    """
    if n <= 0:
        return 0
    return max(wis_iterative(input, n-1), input[n] + wis_iterative(input, n-2))


def wis(input, n):
    """
    Use DP to calculate
    """
    results = [0 for _ in range(n + 1)]
    #base case
    results[0] = 0
    results[1] = input[1]

    # calculate max weight
    for i in range(2, n+1):
        results[i] = max(results[i-1], results[i-2]+input[i])

    final_set = []
    #trace back
    idx = n - 1
    while i >= 1:
        #not included
        if results[i] == results[i-1]:
            i -= 1
        else:
            final_set.append(i)
            i -= 2
    return final_set

def test1():
    input = {1:1, 2:4, 3:5, 4:4}
    print(wis(input, len(input)))
    print(wis_iterative(input, len(input)))


def quiz2():
    data = {}
    with open('quiz2') as input:
        number = input.readline()

        for idx, line in enumerate(input, 1):
            data[idx] = int(line)
    final = wis(data)

    result = ""
    for x in [1, 2, 3, 4, 17, 117, 517, 997]:
        if x in final:
            result = result + "1"
        else:
            result = result + "0"
    print(result)

if __name__ == '__main__':
    test1()
    # quiz2()

