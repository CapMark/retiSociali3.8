import snap
import math
import networkx as nx
import random

Graph_snap = snap.LoadEdgeList(snap.PUNGraph, "rete.txt", 0, 1)
Graph_nx = nx.Graph()
for EI in Graph_snap.Edges():
    Graph_nx.add_edge(EI.GetSrcNId(), EI.GetDstNId())

def delta_v_fi(graph, S, u):
    S_with_u = S | {u}
    total_with_u = 0
    for v in graph.nodes():
        min_neighbors_in_S_with_u = min(len(set(graph.neighbors(v)) & S_with_u), math.ceil(graph.degree(v) / 2))
        total_with_u += min_neighbors_in_S_with_u
    total = 0
    for v in graph.nodes():
        min_neighbors_in_S = min(len(set(graph.neighbors(v)) & S), math.ceil(graph.degree(v) / 2))
        total += min_neighbors_in_S
    return total_with_u - total

def cost_seeds_greedy(graph, k, costs):
    setGrafo=set(graph.nodes())
    Sp = set()
    Sd = set()
    print(sorted(setGrafo, key=lambda v: delta_v_fi(graph, Sd, v) / costs[v]))
    budget_used = 0
    while True:
        try:
            u = max(setGrafo - Sd, key=lambda v: delta_v_fi(graph, Sd, v) / costs[v])
            if delta_v_fi(graph, Sd, u)<=0:
                break
            if sum(costs[v] for v in Sd) + costs[u] <= k:
                Sp = Sd
                Sd = Sp.union({u})
                budget_used += costs[u]
                print("Budget utilizzato:", budget_used)
                if budget_used==k:
                    break
                print(Sd)
            else:
                discard=set()
                discard.add(u)
                setGrafo=setGrafo-discard
        except:
            break
    return Sd
random.seed(42)
costs = {node: random.randint(5, 10) for node in Graph_nx.nodes()}

k = 150
print("Budget="+str(k))
seed_set = cost_seeds_greedy(Graph_nx, k, costs)
print("Seed set selezionato:", seed_set)
