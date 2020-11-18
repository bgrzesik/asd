# https://faliszew.github.io/algograf/lab3
# Bartłomiej Grzesik (jest dwóch Bartłomieji :) )

from dimacs import loadWeightedGraph, readSolution
from queue import PriorityQueue
import math


def merge(G, a, b):
    for u, c in G[b].items():
        if u == a:
            del G[a][b]
            continue

        if u not in G[a]:
            G[u][a] = c
            G[a][u] = c
        else:
            G[a][u] += c
            G[u][a] += c

        del G[u][b]

    G[b] = None


def min_adj_search(V, G):
    A = {1}

    Q = PriorityQueue()
    S = [0] * len(G)  # support :)
    for u, cost in G[1].items():
        Q.put((-cost, u))
        Q.put((-cost, 1))
        S[u] = cost

    last = 1

    while len(A) < V:
        #print(Q.queue, A, V)
        _, u = Q.get_nowait()

        if u in A or G[u] is None:
            continue

        if len(A) >= V - 1:
            return last, u, S[u]

        for v, cost in G[u].items():
            S[v] += cost
            Q.put((-S[v], v))
            Q.put((-S[v], u))

        A.add(u)
        last = u

    return None, None, math.inf


def stoera_wagnera(V, G):
    result = math.inf
    while V > 1:
        #print(V, G)
        u, v, sum_cost = min_adj_search(V, G)

        merge(G, u, v)

        result = min(result, sum_cost)
        V -= 1

    return result


if __name__ == "__main__":
    V = 6
    L = [
        (1, 2, 1), (1, 3, 1), (2, 3, 1),
        (2, 4, 1), (3, 5, 1), (3, 4, 1),
        (4, 5, 1), (4, 6, 1), (5, 6, 1)
    ]
    G = [{} for i in range(V+1)]
    G[0] = None

    for u, v, c in L:
        G[u][v] = G[v][u] = c

    print(stoera_wagnera(V, G))
