import networkx as nx
import snap


Graph_snap = snap.LoadEdgeList(snap.PUNGraph, "ProvinceItaliane.txt", 0, 1)
Graph_nx = nx.Graph()
for EI in Graph_snap.Edges():
    Graph_nx.add_edge(EI.GetSrcNId(), EI.GetDstNId())


def majority_dynamical_process(graph, S):
    inf_s = [set(S)]
    prev_inf_s = set(S)
    total_influenced = len(S)  # Numero totale di nodi influenzati
    r = 0  # Contatore di iterazioni

    while True:
        inf_r = set()
        for node in graph.nodes():
            if node not in prev_inf_s:  # Se il nodo non è stato influenzato negli step precedenti
                neighbors = set(graph.neighbors(node))
                count_influenced_neighbors = len(neighbors.intersection(prev_inf_s))
                if count_influenced_neighbors >= len(neighbors) / 2:
                    inf_r.add(node)

        # Se non ci sono nuovi nodi influenzati, interrompi il processo
        if not inf_r:
            break

        # Aggiorna inf_s con l'insieme di nodi influenzati al passo corrente
        inf_s.append(inf_r)
        prev_inf_s = prev_inf_s.union(inf_r)
        total_influenced += len(inf_r)  # Aggiorna il numero totale di nodi influenzati
        r += 1  # Incrementa il contatore di iterazioni

    return inf_s, total_influenced


# Esempio di utilizzo del codice
if __name__ == "__main__":
    seed_set = {1, 131, 4, 5, 8, 140, 13, 15, 17, 18, 21, 150, 23, 24, 26, 32, 40, 169, 42, 170, 44, 51, 52, 58, 60, 189, 65, 66, 67, 70, 201, 214, 95, 100, 231, 232, 233, 106, 		 113}

    # Calcola Inf[S, r] utilizzando Majority Dynamical Process
    inf_s, total_influenced = majority_dynamical_process(Graph_nx, seed_set)
    # Stampare i risultati
    for r in range(len(inf_s)):
        activated_nodes = sorted(inf_s[r])
        print(f"Iterazione {r}:")
        print(f"  Inf[S, {r}] = {activated_nodes}")
        print(f"  Numero di nodi attivati in Inf[S, {r}]: {len(activated_nodes)} / {len(Graph_nx)}")

    print(f"\nNumero totale di nodi influenzati: {total_influenced}")
    tot=[]
    for list in inf_s:
        tot+=list
    print(tot)
