from graph_util import mat_to_dot
from dataclasses import dataclass, asdict
from priority_queue import heap_add, heap_pop
from typing import Type
import math


@dataclass
class Node:
    station: bool = False

    d: list = None
    parent: list = None


def how_to_get_there(G, P, d, s, t):
    n = len(G)
    nodes = [Node(d=[math.inf] * (d + 1), parent=[None] * (d + 1))
             for _ in range(n)]

    for station in P:
        nodes[station].station = True
        # nodes[station].fuel = d

    queue = []
    heap_add(queue, (0, s, d))

    # nodes[s].fuel = d
    nodes[s].d = [0] * (d + 1)
    nodes[s].parent = [[] for _ in range(d + 1)]

    while len(queue) != 0:
        _, v, fuel = heap_pop(queue)
        vv = nodes[v]

        for u in range(n):
            if G[v][u] == -1:
                continue

            uu = nodes[u]

            dd = vv.d[fuel] + G[v][u]
            ff = fuel - G[v][u]

            if ff >= 0 and uu.d[ff] > dd:
                if uu.station:
                    ff = d

                uu.d[ff] = dd
                uu.parent[ff] = vv.parent[fuel] + [v]
                heap_add(queue, (-dd, u, ff))

    fuel = min(enumerate(nodes[t].d), key=lambda e: e[1])[0]
    return nodes[t].parent[fuel]


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
