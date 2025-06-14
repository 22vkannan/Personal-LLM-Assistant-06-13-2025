import networkx as nx
import matplotlib.pyplot as plt

def create_memory_graph(mem_list):
    G = nx.Graph()
    for idx, text in enumerate(mem_list):
        G.add_node(idx, label=text[:30])
        if idx > 0: G.add_edge(idx-1, idx)
    nx.draw(G, with_labels=True)
    plt.savefig("ui/static/memory_graph.png")
