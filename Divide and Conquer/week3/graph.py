
class Edge():
    def __init__(self, v, w):
        self.v = v
        self.w = w

class Graph():
    def __init__(self, file):
        self.__graph = []
        with open('inputGraph') as data:
            for line in data:
                values = map(int, line.split())
                node_edges = []
                for node in values[1:]:
                    node_edges.append(Edge(values[0], node))
                self.__graph.append(node_edges)

import random
graph = {}

with open('inputGraph') as data:
    for line in data:
        values = map(int, line.split())
        graph[values[0]] = values[1:]
init_graph = graph.copy()

def merge(graph):
    fnode = random.choice(graph.keys())
    snode = random.choice(graph[fnode])
    # print fnode
    # print snode
    # print graph[fnode]
    # print graph[snode]
    graph[fnode] = filter(lambda a: a != snode, graph[fnode])
    graph[snode] = filter(lambda a: a != fnode, graph[snode])
    for node in graph[snode]:
        try:
            graph[node] = [fnode if x == snode else x for x in graph[node]]
        except KeyError:
            print('WARNING')
            print graph.keys()
            print node
            print fnode
            print snode
            print graph[fnode]
            print graph[snode]
            print('WARNING')
            exit()
        graph[fnode].append(node)
    graph.pop(snode)


min_cut = 200
for x in range(0,200):
    graph = init_graph.copy()
    while len(graph.keys())>2:
        merge(graph)
    for key in graph.keys():
        cut = len(graph[key])
        min_cut = cut if cut < min_cut else min_cut

print min_cut
