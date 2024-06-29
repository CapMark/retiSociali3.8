import networkx as nx
import matplotlib.pyplot as plt
import re
def read_graph_from_file(file_path):
    """
    Legge un grafo da un file di testo.

    :param file_path: Il percorso del file di testo.
    :return: Un oggetto di tipo networkx.Graph.
    """
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            edge = line.strip().split()
            if len(edge) == 2:
                node1, node2 = map(int, edge)  # Converte i nodi in interi
                G.add_edge(node1, node2)
    return G

def draw_graph(G, red_nodes=None, purple_nodes=None):
    """
    Disegna il grafo utilizzando matplotlib.

    :param G: Un oggetto di tipo networkx.Graph.
    :param red_nodes: Lista dei nodi da colorare di rosso.
    :param purple_nodes: Lista dei nodi da colorare di viola.
    """
    pos = nx.spring_layout(G)
    node_color = []
    for node in G.nodes():
        if red_nodes and node in red_nodes:
            node_color.append('red')
        elif purple_nodes and node in purple_nodes:
            node_color.append('purple')
        else:
            node_color.append('skyblue')
    nx.draw(G, pos, with_labels=False, node_color=node_color, edge_color='gray', node_size=200, font_size=20)
    plt.show()

def main(file_path, red_nodes, purple_nodes):
    """
    Legge un grafo da un file e lo disegna.

    :param file_path: Il percorso del file di testo.
    :param red_nodes: Lista dei nodi da colorare di rosso.
    :param purple_nodes: Lista dei nodi da colorare di viola.
    """
    G = read_graph_from_file(file_path)
    draw_graph(G, red_nodes, purple_nodes)

# Esempio di utilizzo
file_path = 'ProvinceItaliane.txt'  # Sostituisci con il percorso del tuo file
red_nodes = [1, 131, 4, 5, 8, 140, 13, 15, 17, 18, 21, 150, 23, 24, 26, 32, 40, 169, 42, 170, 44, 51, 52, 58, 60, 189, 65, 66, 67, 70, 201, 214, 95, 100, 231, 232, 233, 106,113]  # Nodi da colorare di rosso
purple_nodes = [1, 131, 4, 5, 8, 140, 13, 15, 17, 18, 21, 150, 23, 24, 26, 32, 40, 169, 42, 170, 44, 51, 52, 58, 60, 189, 65, 66, 67, 70, 201, 214, 95, 100, 231, 232, 233, 106, 		 113, 64, 97, 2, 96, 68, 99, 7, 39, 10, 12, 16, 19, 20, 22, 55, 54, 59, 63, 3, 6, 9, 74, 11, 45, 14, 46, 77, 50, 29, 62, 36, 38, 43, 57, 61, 30, 35, 72, 49, 53, 		 25, 27, 56, 28, 37, 71, 48, 34, 69, 33, 73, 41, 108, 31, 83, 76, 47]


main(file_path, red_nodes, purple_nodes)
