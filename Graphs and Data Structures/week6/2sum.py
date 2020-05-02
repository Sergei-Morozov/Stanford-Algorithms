"""
 compute the number of target values t in the interval [-10000,10000]
 (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t
"""


def calc_sum_naive(input):
    """
    - put input to map
    - iterate input
    - for each t [-10000,10000] check if second value also in hash map
    """
    hashmap = set(input)
    t_list = {t for t in range(-10000, 10001)}
    result = set()
    print("start")
    # should satisfy x+y=t
    for t in t_list:
        for x in input:
            y = t - x
            if y != x and y in hashmap:
                result.add(t)
    return result

def calc_sum_2ptr(input):
    """
    - sort array
    - move pointer_head ->[-10000, 10000]<-pointer_tail
        - for every pair head and tail check possible sums
        - move head+1 or tail-1
    -continue while head > tail
    """
    result = set()
    data = sorted(input)
    size = len(data)

    targets= [range(-10000,10001)]

    head_idx = 0
    tail_idx = size - 1

    while head_idx < tail_idx:
        pair_sum = data[head_idx] + data[tail_idx]
        if pair_sum < -10000:
            head_idx += 1
        elif pair_sum > 10000:
            tail_idx -= 1
        else:
            for i in range(head_idx, tail_idx+1):
                if data[i] != data[tail_idx]:
                    new_sum = data[i] + data[tail_idx]
                    if new_sum < 10000:
                        result.add(new_sum)
                    else:
                        break

            for i in range(tail_idx, head_idx, - 1):
                if data[i] != data[head_idx]:
                    new_sum = data[i] + data[head_idx]
                    if new_sum > -10000:
                        result.add(new_sum)
                    else:
                        break
            head_idx += 1

    return result

def test():
    """
    simple test
    """
    input = [1,2,3]

    expected_output = {3,4,5}
    assert calc_sum_naive(input) == expected_output
    assert calc_sum_2ptr(input) == expected_output

test()
def quiz1():
    """
    -read file
    -calculate distinct t
    """
    with open("quiz1") as data:
        input = [int(line) for line in data]

    print(len(calc_sum_2ptr(input)))
quiz1()
