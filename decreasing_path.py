from graph_util import adj_to_dot
from dataclasses import dataclass, field
from priority_queue import heap_add, heap_pop
import math


@dataclass
class Node:
    adj: list = field(default_factory=list)
    parent: int = None
    d: int = math.inf
    path: list = None


def biggest(G, s, t):
    queue = [(0, math.inf, s)]

    for v in G:
        v.adj.sort(key=lambda e: e[1])

    G[s].d = 0
    G[s].parent = None

    while len(queue) != 0:
        d, l, u = heap_pop(queue)
        print(d, l, u, queue)
        d = -d

        uu = G[u]
        uu.d = min(uu.d, d)

        # if u == t:
        #     break

        for v, w in uu.adj:
            if w < l:
                heap_add(queue, (-(d + w), w, v))

    return G[t].d


if __name__ == "__main__":
    G = [Node(adj=[(1, 20), (2, 10), (3, 3)]),
         Node(adj=[(0, 20), (3, 16)]),
         Node(adj=[(0, 10), (3, 17), (4, 15)]),
         Node(adj=[(0, 3), (1, 16), (2, 17), (4, 15), (5, 18)]),
         Node(adj=[(2, 15), (3, 15), (5, 14)]),
         Node(adj=[(3, 18), (4, 14)])]

    print(adj_to_dot(G,
                     edge_info=lambda _, e: f'label="{e[1]}"',
                     vex_to_adj=lambda v: v.adj,
                     edge_to_idx=lambda e: e[0]))

    print(biggest(G, 0, 5))
