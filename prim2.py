from priority_queue import heap_add, heap_pop
from graph_util import unmat_to_dot
import math


def prim(G):
    n = len(G)
    weight = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    weight[0] = 0
    queue = []
    heap_add(queue, (0, 0))

    while len(queue) != 0:
        w, vidx = heap_pop(queue)

        if visited[vidx]:
            continue

        visited[vidx] = True

        for uidx in range(len(G)):
            if G[vidx][uidx] == 0 or visited[uidx]:
                continue

            if weight[uidx] > G[vidx][uidx]:
                weight[uidx] = G[vidx][uidx]
                parent[uidx] = vidx
                heap_add(queue, (-weight[uidx], uidx))

    print(unmat_to_dot(G,
                       edge_exists=lambda e: e != 0,
                       vex_info=lambda vidx: {"label": {"id": vidx,
                                                        "weight": weight[vidx],
                                                        "parent": parent[vidx]}},
                       edge_info=lambda vidx, uidx, e: {"label": {"w": e, },
                                                        "color": "red" if parent[vidx] == uidx or parent[uidx] == vidx else "black"}))
    mst = []
    for i in range(1, n):
        mst.append((i, parent[i]))

    return mst, sum([G[v][u] for v, u in mst])


if __name__ == "__main__":
    G = [
        [0, 4, 8, 0, 0, 0, 0, 0, 0],
        [4, 0, 11, 8, 0, 0, 0, 0, 0],
        [8, 11, 0, 0, 0, 0, 0, 1, 7],
        [0, 8, 0, 0, 7, 0, 4, 0, 2],
        [0, 0, 0, 7, 0, 9, 14, 0, 0],
        [0, 0, 0, 0, 9, 0, 10, 0, 0],
        [0, 0, 0, 4, 14, 10, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 2, 0, 6],
        [0, 0, 7, 2, 0, 0, 0, 6, 0],
    ]
    print(prim(G))
