from graph_util import mat_to_dot
import math


def maxflow(G, s, t):
    n = len(G)

    F = [[0 if G[u][v] or G[v][u] else None
          for v in range(n)] for u in range(n)]

    def cf(uidx, vidx):
        nonlocal G, F
        if G[uidx][vidx] is not None:
            return G[uidx][vidx] - F[uidx][vidx]
        elif G[vidx][uidx] is not None:
            return F[uidx][vidx]
        else:
            return 0

    while True:
        parents = [None] * n
        visited = [False] * n

        queue = [s]
        visited[s] = True
        flow = math.inf

        while len(queue) != 0:
            u = queue.pop()

            for v in range(n):
                f = cf(u, v)
                if f == 0:
                    continue
                if not visited[v]:
                    visited[v] = True
                    parents[v] = u
                    queue.append(v)
                    flow = min(flow, f)

        if not visited[t]:
            break

        a = t
        while parents[a] is not None:
            F[parents[a]][a] += flow
            print(parents[a], a)
            a = parents[a]

    print(mat_to_dot(F,
                     vex_info=lambda v: {"label": {"id": v}},
                     edge_info=lambda v, u, e: {"fontsize": 5,
                                                "label": {
                                                    "c": G[v][u],
                                                    "f": F[v][u],
                                                    "cf": cf(v, u),
                                                }}))

    return F


if __name__ == "__main__":
    G = [
        [None, 4, 3, None, None, None],
        [None, None, 2, None, 2, None],
        [None, None, None, 2, 2, None],
        [None, None, None, None, None, 5],
        [None, None, None, None, None, 4],
        [None, None, None, None, None, None],
    ]

    print(mat_to_dot(G,
                     vex_info=lambda vidx: f'label="id={vidx}"',
                     edge_info=lambda vidx, uidx, e: f'label="c={e}"'))
    print(maxflow(G, 0, 5))
