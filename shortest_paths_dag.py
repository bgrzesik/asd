
from graph_util import mat_to_dot
from dataclasses import dataclass, field
import math


@dataclass
class Node:
    pred: int = 0
    parent: int = 0
    d: int = math.inf


def shortest_dag(G, s):
    n = len(G)
    nodes = [Node() for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                nodes[v].pred += 1

    def dfs_visit(u):
        nonlocal G, nodes

        for v in range(n):
            if G[u][v] == 0:
                continue

            if nodes[v].d > nodes[u].d + G[u][v]:
                nodes[v].d = nodes[u].d + G[u][v]
                nodes[v].parent = u

            nodes[v].pred -= 1

            if nodes[v].pred == 0:
                dfs_visit(v)

    nodes[s].d = 0
    dfs_visit(s)

    print(mat_to_dot(G,
                     vex_info=lambda v: f'label="id={v}\\nparent={nodes[v].parent}\\nd={nodes[v].d}\\npred={nodes[v].pred}"',
                     edge_info=lambda v, u, e: f'label="{e}"',
                     edge_exists=lambda e: e != 0,))


if __name__ == "__main__":
    G = [
        [0, 1, 0, 0, 10, 12, 0, 0, 0],
        [0, 0, 1, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 1, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 3, 5, 7],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    print(shortest_dag(G, 0))
