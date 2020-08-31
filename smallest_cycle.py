import math


def smallest_cycle(G):
    n = len(G)

    for u in range(n):
        for v in range(n):
            for x in range(n):
                if G[u][v] > G[u][x] + G[x][v]:
                    G[u][v] = G[u][x] + G[x][v]

    return min([G[i][i] for i in range(len(G))])


if __name__ == "__main__":
    inf = math.inf
    G = [[inf, 1, inf, inf, inf, inf, 2, inf, inf],
         [inf, inf, 1, inf, inf, inf, inf, inf, inf],
         [inf, inf, inf, 1, inf, inf, inf, inf, inf],
         [2, inf, inf, inf, 1, inf, inf, inf, inf],
         [inf, inf, inf, inf, inf, 1, inf, inf, inf],
         [inf, inf, inf, inf, inf, inf, 1, inf, inf],
         [inf, inf, inf, 2, inf, inf, inf, 1, inf],
         [inf, inf, inf, inf, inf, inf, inf, inf, 1],
         [1, inf, inf, inf, inf, inf, inf, inf, inf], ]

    print(smallest_cycle(G))
