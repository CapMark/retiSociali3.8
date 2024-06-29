import snap
import math
import networkx as nx
import random

Graph_snap = snap.LoadEdgeList(snap.PUNGraph, "rete.txt", 0, 1)
Graph_nx = nx.Graph()
for EI in Graph_snap.Edges():
    Graph_nx.add_edge(EI.GetSrcNId(), EI.GetDstNId())

def f2(graph, S):
    total_influence = 0
    for v in graph.nodes():
        num_neighbors_in_S = len(set(graph.neighbors(v)) & S)
        dv = math.ceil(graph.degree(v) / 2)
        influence = sum(max(dv - i + 1, 0) for i in range(1, num_neighbors_in_S + 1))
        total_influence += influence
    return total_influence

def delta_v_fi_f2(graph, S, u):
    S_with_u = S | {u}
    return f2(graph, S_with_u) - f2(graph, S)

def cost_seeds_greedy_f2(graph, k, costs):
    setGrafo = set(graph.nodes())
    Sp = set()
    Sd = set()
    print(sorted(setGrafo, key=lambda v: delta_v_fi_f2(graph, Sd, v) / costs[v]))
    budget_used = 0
    while True:
        try:
            u = max(setGrafo - Sd, key=lambda v: delta_v_fi_f2(graph, Sd, v) / costs[v])
            if delta_v_fi_f2(graph, Sd, u)<=0:
                break
            if sum(costs[v] for v in Sd) + costs[u] <= k:
                Sp = Sd
                Sd = Sp.union({u})
                budget_used += costs[u]
                print("Budget utilizzato:", budget_used)
                if budget_used == k:
                    break
                print(Sd)
            else:
                discard = set()
                discard.add(u)
                setGrafo = setGrafo - discard
        except:
            break
    return Sd

costs = {node: Graph_nx.degree(node)/2 for node in Graph_nx.nodes()}
k = 150
print("Budget="+str(k))
seed_set_f2 = cost_seeds_greedy_f2(Graph_nx, k, costs)
print("Seed set selezionato con f2(S):", seed_set_f2)
