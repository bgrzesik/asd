import math


def islands(G, A, B):
    n = len(G)

    D = [math.inf] * n
    P = [None] * n

    D[A] = 0

    for _ in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0 and G[u][v] != P[u]:
                    if D[v] > D[u] + G[u][v]:
                        D[v] = D[u] + G[u][v]
                        P[v] = G[u][v]

    return D[B]
