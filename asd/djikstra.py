from queue import PriorityQueue


class Node(object):
    def __init__(self):
        self.d = float("+inf")
        self.parent = None
        self.visited = False

    def __repr__(self):
        return f"({self.d} {self.parent is None} {self.visited})"


def djikstra(G, s, t):
    queue = PriorityQueue()
    nodes = [Node() for _ in range(len(G))]

    nodes[0].d = 0
    queue.put((0, s))

    while not queue.empty():
        _, v_idx = queue.get()
        v = nodes[v_idx]
        v.visited = True

        for u_idx in range(len(G)):
            if G[v_idx][u_idx] is None or nodes[u_idx].visited:
                continue

            u = nodes[u_idx]

            if u.d > v.d + G[v_idx][u_idx]:
                u.d = v.d + G[v_idx][u_idx]
                u.parent = v
                queue.put((u.d, u_idx))

    return nodes[t].d


if __name__ == "__main__":
    G = [
        # s   t   x   y   z
        [None, 10, None, 5, None],  # s
        [None, None, 1, 2, None],  # t
        [None, None, None, None, 4],  # x
        [None, 3, 9, None, 2],  # y
        [7, None, 6, None, None],  # z
    ]
    print(djikstra(G, 0, 4))
