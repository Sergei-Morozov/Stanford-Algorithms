"""
Bellman-Ford shortest path computation

Input: directed graph G=(V,E)

Output:
    - negative cycle
    - shortest path


"""
def draw_graph(graph):
    """
    Function to visualise graph (adj list) with matplotlib
    """
    import networkx as nx
    import matplotlib
    import matplotlib.pyplot as plt

    G = nx.DiGraph(graph)
    nx.draw_networkx(G, with_labels = True, node_color = "c", edge_color = "k", font_size = 8, arrows=True)

    plt.axis('off')
    plt.draw()
    plt.show()

def bellman_ford(input, start):
    """
    L(i,v) = min   -  L(i-1,v)
                   -  for (w,v e E)
                         min{ L(i-1,w) + C(w,v) }
    - where i number of edges to use (to max n)

    """
    distance = {k:float('inf') for k in input}
    distance[start] = 0

    for i in range(len(input)):
        for head in input:
            for tail in input[head]:
                weight = input[head][tail]
                if distance[head] != float('inf') and distance[tail] > distance[head] + weight:
                    distance[tail] = distance[head] + weight

    # one more iteration to detect cycle
    for head in input:
        for tail in input[head]:
            weight = input[head][tail]
            if distance[head] != float('inf') and distance[tail] > distance[head] + weight:
                print("negate cycle detected")
                exit()

    return distance

if __name__ == '__main__':
    g = []

    g = {
        0: {1: -1, 2: 4},
        1: {2:3, 3:2, 4: 2},
        2: {},
        3: {2:5, 1:1},
        4: {3:-3},
    }


    # draw_graph(g)
    result = bellman_ford(g, 0)

    print(result)


    # Vertex   Distance from Source
    # 0                0
    # 1                -1
    # 2                2
    # 3                -2
    # 4                1
