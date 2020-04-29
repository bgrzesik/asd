def tclosure(G):
    G = [g.copy() for g in G]

    n = len(G)

    for t in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = G[i][j] or (G[i][t] and G[t][j])

    return G


if __name__ == "__main__":
    G = [[False, True, False],
         [False, False, True],
         [False, False, False]]

    print(tclosure(G))
