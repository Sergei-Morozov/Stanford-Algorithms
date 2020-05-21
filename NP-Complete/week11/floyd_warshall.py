"""
Floyd-Warshall

- define order of vertices
    V(k) = { 1,2 ... k}

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

def floyd_warshall(graph):
    """
    -create 2d array of distances between 2 vertices dist[i][j]
    -set initial weight as w(i,j)
    -iterate over 1...k nodes - relax distance if its shorter
    """
    n = len(graph)
    dist=[[float('inf') for _ in range(n)] for _ in range(n)]

    for head in graph:
        dist[head][head] = 0
        for tail in graph[head]:
            dist[head][tail] = graph[head][tail]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    return dist
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
    result = floyd_warshall(g)

    print(result)

    # Vertex   Distance from Source
    # 0                0
    # 1                -1
    # 2                2
    # 3                -2
    # 4                1


