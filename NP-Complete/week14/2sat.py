"""
Local search with 2sat

Input:
- n boolean variables : [x1, x2, x3 ..., xn]
- m clause of 2 literals each % "literal" := x1 or not x3

Output:
    - variable values thet makes all m clauses == True

Details:
    - Papadimitriou (local search)
    - Backtracking
    - Strongly connected components

"""
import math
import random
def local_2sat(n, m):
    """
    Repeat log2(n) times:
        - choose random assignment
        - Repeat 2n^2:
            - if worked - return
            - pick unsatisfied clause and flip 1 variable choosed randomly
    """
    size = len(n)//2

    for i in range(int((math.log(size, 2)))):

        # flip value randomly (both x and not x)
        for x in range(1, size+1):
            value = bool(random.randrange(2))
            n[x] = value
            n[-x] = not value
        for j in range(2*(size**2)):
            # check clause in randomly shuffled array
            random.shuffle(m)
            for item in m:
                if not (n[item[0]] or n[item[1]]):
                    # flip chossed var (x and not x together)
                    flip = random.randrange(2)
                    n[item[flip]] = not n[item[flip]]
                    n[-item[flip]] = not n[-item[flip]]
                    break
            else:
                # no break - means all true
                return True
    return False

from scc import scc

def scc_2sat(size, m):
    """
    AvB = True as: (not A => B) or  (not B => A) as graph edges
    """
    graph = {k:[] for k in range(-size, size+1)}
    graph.pop(0)

    for a,b in m:
        graph[-a].append(b)
        graph[-b].append(a)

    # determine scc, if in single scc both a and not a -> return false

    components = scc(graph)

    # check in each component a and not a
    for comp in components:
        vertices = set(comp)
        for v in vertices:
            if -v in vertices:
                return False
    return True



def test_quiz(input):
    with open(input) as file:
        number = int(file.readline())

        # init all vars to false both x and not x
        n = [False for _ in range(-number, number+1)]
        # init clause list
        m = []
        for line in file:
            n1, n2 = map(int, line.split())
            m.append((n1, n2))
        # result = local_2sat(n, m)
        # print(result)
        result = scc_2sat(number, m)
        print(result)

test_quiz('2sat1')
test_quiz('2sat2')
test_quiz('2sat3')
test_quiz('2sat4')
test_quiz('2sat5')
test_quiz('2sat6')
