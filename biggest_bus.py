
from dataclasses import dataclass, field
from priority_queue import heap_add, heap_pop
import math


@dataclass
class Node:
    adj: list = field(default_factory=list)
    n: int = -math.inf
    parent: int = None


def biggest(G, s, t):
    queue = []
    queue.append((math.inf, s))
    G[s].parent = None
    G[s].n = math.inf

    while len(queue) != 0:
        _, u = heap_pop(queue)
        uu = G[u]
        for v, n in uu.adj:
            vv = G[v]

            if vv.n < min(uu.n, n):
                vv.n = min(uu.n, n)
                vv.parent = u

                heap_add(queue, (vv.n, v))

    return G[t].n


if __name__ == "__main__":
    G = [Node(adj=[(1, 20), (2, 10), (3, 3)]),
         Node(adj=[(0, 20), (3, 16)]),
         Node(adj=[(0, 10), (3, 17), (4, 15)]),
         Node(adj=[(0, 3), (1, 16), (2, 17), (4, 20), (5, 18)]),
         Node(adj=[(2, 15), (3, 20), (5, 14)]),
         Node(adj=[(3, 18), (4, 14)])]

    print(biggest(G, 0, 5))
