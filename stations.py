from graph_util import mat_to_dot
from dataclasses import dataclass, asdict
from priority_queue import heap_add, heap_pop
from typing import Type
import math


@dataclass
class Node:
    station: bool = False
    parent: int = None
    fuel: int = 0
    d: int = math.inf


def how_to_get_there(G, P, d, s, t):
    n = len(G)
    nodes = [Node() for _ in range(n)]

    for station in P:
        nodes[station].station = True
        nodes[station].fuel = d

    queue = []
    heap_add(queue, (0, s))

    nodes[s].fuel = d
    nodes[s].d = 0

    print(mat_to_dot(G, vex_info=lambda v: {"label": {**{"id": v}, **asdict(nodes[v])}},
                     edge_exists=lambda e: e != -1,
                     edge_info=lambda u, v, e: {"label": {"d": e}}))

    while len(queue) != 0:
        _, v = heap_pop(queue)
        vv = nodes[v]

        for u in range(n):
            if G[v][u] == -1:
                continue

            uu = nodes[u]

            dd = vv.d + G[v][u]
            if ((uu.d > dd) or (uu.d == dd and uu.fuel < vv.fuel - G[v][u])) and G[v][u] <= vv.fuel:
                uu.d = dd
                uu.fuel = max(uu.fuel, vv.fuel - dd)
                uu.parent = v
                heap_add(queue, (-uu.d, u))

    if nodes[t].parent is None:
        return None

    path = []
    a = t
    while nodes[a].parent is not None:
        path.insert(0, a)
        a = nodes[a].parent
    path.insert(0, a)

    return path


if __name__ == "__main__":
    G = [[-1, 6, -1, 5, 2],
         [-1, -1, 1, 2, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, 4, -1, -1],
         [-1, -1, 8, -1, -1]]
    P = [0, 1, 3]

    print(how_to_get_there(G, P, 5, 0, 2))
    print(how_to_get_there(G, P, 6, 0, 2))
    print(how_to_get_there(G, P, 3, 0, 2))
