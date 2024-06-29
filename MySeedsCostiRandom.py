import snap
import math
import networkx as nx
import random


Graph_snap = snap.LoadEdgeList(snap.PUNGraph, "rete.txt", 0, 1)
Graph_nx = nx.Graph()
for EI in Graph_snap.Edges():
    Graph_nx.add_edge(EI.GetSrcNId(), EI.GetDstNId())

def my_seeds_betweenness(graph, k, costs):
    S = set()
    budget_used = 0
    betweenness = nx.betweenness_centrality(graph)
    nodes_sorted_by_betweenness = sorted(betweenness, key=betweenness.get, reverse=True)
    for node in nodes_sorted_by_betweenness:
        if budget_used + costs[node] > k:
            break
        S.add(node)
        budget_used += costs[node]
        print("Budget utilizzato:", budget_used)
        print(S)
    return S
random.seed(42)
costs = {node: random.randint(5, 10) for node in Graph_nx.nodes()}
k = 150
print("Budget="+str(k))
seed_set = my_seeds_betweenness(Graph_nx, k, costs)
print("Seed set selezionato:", seed_set)
