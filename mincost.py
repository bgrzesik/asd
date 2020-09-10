import math


def mincost(G, C, max_flow, s, t):
    n = len(G)
    F = [[0] * n for _ in range(n)]

    def bellman_ford():
        nonlocal G, s, t, n
        D = [math.inf] * n
        P = [None] * n
        M = [math.inf] * n

        D[s] = 0
        for _ in range(n):
            for i in range(n):
                for j in range(n):
                    c = C[i][j] if G[i][j] != 0 else -C[j][i]
                    u = G[i][j] - F[i][j] if G[i][j] != 0 else F[j][i]

                    if u == 0:
                        continue

                    if D[j] > D[i] + c:
                        D[j] = D[i] + c
                        P[j] = i
                        M[j] = min(M[i], u)

        return P, M[t], D[t]

    overall_flow = 0
    overall_cost = 0
    P, flow, cost = bellman_ford()

    while P[t] is not None:
        flow = min(flow, max_flow - overall_flow)
        overall_flow += flow
        overall_cost += cost * flow

        a = t
        while P[a] is not None:
            if G[P[a]][a] != 0:
                F[P[a]][a] += flow
            else:
                F[P[a]][a] -= flow

            a = P[a]

        if overall_flow == max_flow:
            break

        P, flow, cost = bellman_ford()

    return overall_flow, overall_cost


if __name__ == "__main__":
    G = [[0, 3, 4, 5, 0],
         [0, 0, 2, 0, 0],
         [0, 0, 0, 4, 1],
         [0, 0, 0, 0, 10],
         [0, 0, 0, 0, 0]]

    C = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

    print(mincost(G, C, math.inf, 0, 4))

    G = [[0, 3, 1, 0, 3],
         [0, 0, 2, 0, 0],
         [0, 0, 0, 1, 6],
         [0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0]]
    C = [[0, 1, 0, 0, 2],
         [0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

    print(mincost(G, C, math.inf, 0, 4))
    print(mincost(G, C, 3, 0, 4))
