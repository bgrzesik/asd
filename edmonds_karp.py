

def edmonds_karp(G, s, t):
    n = len(G)
    flow = 0
    parent = None

    f = [[0] * n for _ in range(n)]

    while parent is None or parent[t] is not None:
        Q = [s]

        parent = [None] * n

        while len(Q) != 0:
            u = Q.pop()

            for v, w in enumerate(G[u]):
                if w is None:
                    continue

                if parent[v] is None and v != s and f[u][v] < w:
                    parent[v] = u
                    Q.insert(0, v)

        if parent[t] is not None:
            profit = float("+inf")

            i = t
            while parent[i] is not None and i != s:
                profit = min(profit, G[parent[i]][i] - f[parent[i]][i])
                i = parent[i]

            i = t
            while parent[i] is not None and i != s:
                f[parent[i]][i] += profit
                f[i][parent[i]] -= profit
                i = parent[i]

    return f


if __name__ == "__main__":
    from pprint import pprint

    G = [
        #  s    v1    v2    v3    v4    t
        [None,   16,   13, None, None, None],  # s
        [None, None, None,   12, None, None],  # v1
        [None,    4, None, None,   14, None],  # v2
        [None, None,    9, None, None,   20],  # v3
        [None, None, None,    7, None,    4],  # v4
        [None, None, None, None, None, None],  # t
    ]

    f = edmonds_karp(G, 0, 5)
    pprint(sum(f[0]))
    pprint(f)
