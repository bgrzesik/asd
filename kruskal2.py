from graph_util import unmat_to_dot
from priority_queue import heap_add, heap_pop


def find(i, parents):
    if parents[i] == i:
        return i
    else:
        parents[i] = find(parents[i], parents)
        return parents[i]


def union(i, j, ranks, parents):
    i = find(i, parents)
    j = find(j, parents)

    if ranks[i] > ranks[j]:
        parents[j] = i
    else:
        parents[i] = j
        if ranks[i] == ranks[j]:
            ranks[j] += 1


def kruskal(G):
    n = len(G)
    ranks = [0 for _ in range(n)]
    parents = [i for i in range(n)]

    queue = []

    for vidx in range(1, n):
        for uidx in range(vidx):
            if G[vidx][uidx] is not None and G[vidx][uidx] != 0:
                heap_add(queue, (-G[vidx][uidx], vidx, uidx))

    mst = []
    while len(queue) != 0:
        w, vidx, uidx = heap_pop(queue)
        w = -w

        if find(vidx, parents) != find(uidx, parents):
            mst.append((vidx, uidx))
            union(vidx, uidx, ranks, parents)

    print(unmat_to_dot(G,
                       edge_exists=lambda e: e != 0,
                       vex_info=lambda vidx: {"label": {"id": vidx,
                                                        "parent": parents[vidx],
                                                        "ranks": ranks[vidx]}},
                       edge_info=lambda vidx, uidx, e: {"label": {"w": e, },
                                                        "color": "red" if (vidx, uidx) in mst else "black"}))

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
    print(kruskal(G))
