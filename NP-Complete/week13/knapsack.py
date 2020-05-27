"""
Approximation algo for knapsack,
First implement another approach for knapsack problem
matrix iteratin over items and values and storing weights


Input:
    n items
    - value vi
    - size wi
    - capacity x
Ouput:
    - subset of n that maximize value

Details:
    use - 2D array (items, n*Vmax), so n*vmax is max capacity ever possible
    A[0,x] = 0 for all x
    A[i,x] = min{A[i-1,x], A[i-1, x-Vi] + vi}
                 exclude   included
            both can be previously computed

    sca matrix return largest x so A[n,x] < capacity
"""
def knapsack_recursive(values, weights, i, capacity):
    if i == 0 or capacity == 0:
        return 0

    return max(knapsack_recursive(values, weights, i-1, capacity),
               weights[i-1] + knapsack_recursive(values, weights, i-1, capacity - weights[i-1]))

def knapsack(values, weights, capacity, e):
    """
    O(n**2 * Vmax)

    - convert values to Vi = Vmax*n/e (reduces vmax)
    - calc array
    """
    n = len(values)

    # caculate approximate Vi as Vmod(m)
    m = max(values)*e/n
    values = [v%m for v in values]
    print(values)
    vmax = int(n * max(values))
    # init array (item, value) := weight
    A = [[float('inf') for value in range(vmax)] for _ in range(n)]

    # assing weight 0 for 0 items and any value
    for v in range(vmax):
        A[0][0] = 0

    for i in range(1, n):
        for v in range(vmax):
            if v < values[i]:
                A[i][v] = A[i-1][v]
            else:
                A[i][v] = min(A[i-1][v], weights[i] + A[i-1][v-values[i]])

    # scan result for max possible weight and overall capacity less then values
    max_weight = float('-inf')
    max_value = None
    for i in range(n):
        for v in range(vmax):
            if A[i][v]!= float('inf') and v <= capacity and max_weight < A[i][v]:
                max_weight = A[i][v]
                max_value = v
    return max_value



def test1():
    values = [6, 10, 12]
    weights = [10, 20, 30]
    capacity = 50

    expected_answer = 22

    result = knapsack_recursive(values, weights, 3, capacity)
    print(result)
    result =  knapsack(values, weights, capacity, 95.0)
    print(result)

test1()
