class Node(object):
    def __init__(self):
        self.d = float("+inf")
        self.parent = None
        self.visited = False

    def __repr__(self):
        return f"({self.d} {self.parent is None} {self.visited})"


def bellman_ford(G, s, t):
    nodes = [Node() for _ in range(len(G))]

    nodes[s].d = 0

    for i in range(len(G)):
        for u_idx in range(len(G)):
            for v_idx in range(len(G)):
                w = G[u_idx][v_idx]

                if w is None:
                    continue

                if nodes[v_idx].d > nodes[u_idx].d + w:
                    nodes[v_idx].d = nodes[u_idx].d + w
                    nodes[v_idx].parent = u_idx

    for u_idx in range(len(G)):
        for v_idx in range(len(G)):
            w = G[u_idx][v_idx]

            if w is None:
                continue

            if nodes[v_idx].d > nodes[u_idx].d + w:
                return None

    path = []
    p = t
    while p is not None:
        path.insert(0, p)
        p = nodes[p].parent

    return path, nodes[t].d


if __name__ == "__main__":
    names = "stxyz"
    G = [
        # s   t   x   y   z
        [None, 10, None, 5, None],  # s
        [None, None, 1, 2, None],  # t
        [None, None, None, None, 4],  # x
        [None, 3, 9, None, 2],  # y
        [7, None, 6, None, None],  # z
    ]

    path, d = bellman_ford(G, 0, 4)

    print(" -> ".join(map(names.__getitem__, path)))
    print(d)

    G = [
        #   s     t     x     y     z
        [None, 6, None, 7, None],  # s
        [None, None, 5, 8, -4],  # t
        [None, -2, None, None, None],  # x
        [None, None, -3, None, 9],  # y
        [2, None, 7, None, None],  # z
    ]

    path, d = bellman_ford(G, 0, 4)

    print(" -> ".join(map(names.__getitem__, path)))
    print(d)
