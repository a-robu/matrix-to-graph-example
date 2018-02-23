from string import ascii_lowercase
import networkx as nx
from sympy import Matrix
from nxpd import draw

def draw_graph(matrix, labels=ascii_lowercase, round_by=2):
    G = nx.DiGraph()
    G.graph['rankdir'] = 'LR'
    for i in range(matrix.cols):
        G.add_node(i, label=labels[i])
    for i in range(matrix.cols):
        for j in range(matrix.rows):
            p = round(matrix[j, i], round_by)
            if p > 0:
                if p < 1:
                    label = str(p)
                    G.add_edge(i, j, label=label, color='grey55')
                else:
                    G.add_edge(i, j)
    return draw(G)

example_matrix = Matrix([
    [0, 0.5, 0, 0.5],
    [1, 0, 0, 0],
    [0, 0.5, 0, 0.5],
    [0, 0, 1, 0]
])

if __name__ == "__main__":
    draw_graph(example_matrix)

