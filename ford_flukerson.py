
def _cf(G, f, u, v):
    if G[u][v] is not None:
        return G[u][v] - f[u][v]
    elif G[v][u] is not None:
        return f[v][u]
    return 0


def _exist_extending_part(G, f, s, t):
    n = len(G)
    parents = [None] * n
    visited = [False] * n
    visited[s] = True

    Q = [s]
    while Q:
        v = Q.pop()

        for u in range(n):
            if _cf(G, f, v, u) == 0:
                continue

            if not visited[u]:
                visited[u] = True
                parents[u] = v
                Q.append(u)

    path = []

    while t is not None:
        if parents[t] is None:
            break

        path.insert(0, (parents[t], t))
        t = parents[t]

    return path


def ford_flukerson(G, s, t):
    n = len(G)
    f = [[0] * n for _ in range(n)]

    while (path := _exist_extending_part(G, f, s, t)):
        profit = min([_cf(G, f, u, v) for u, v in path])

        for u, v in path:
            if G[u][v] is not None:
                f[u][v] += profit
            else:
                f[v][u] -= profit

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

    f = ford_flukerson(G, 0, 5)
    pprint(sum(f[0]))
    pprint(f)
