from queue import PriorityQueue


# O(E + VlogV)

class Node(object):
    def __init__(self):
        self.d = float("+inf")
        self.parent = None
        self.visited = False

    def __repr__(self):
        return f"({self.d} {self.parent is None})"


def djikstra(G, s):
    queue = PriorityQueue()
    nodes = [Node() for _ in range(len(G))]

    nodes[s].d = 0
    queue.put((0, s))

    while not queue.empty():
        _, v_idx = queue.get()
        v = nodes[v_idx]

        if v.visited:
            continue
        v.visited = True

        for u_idx in range(len(G)):
            if G[v_idx][u_idx] is None:
                continue

            u = nodes[u_idx]

            if u.d > v.d + G[v_idx][u_idx]:
                u.d = v.d + G[v_idx][u_idx]
                u.parent = v_idx
                queue.put((u.d, u_idx))

    return list(map(lambda node: node.parent, nodes))


if __name__ == "__main__":
    G = [
        # s   t   x   y   z
        [None, 10, None, 5, None],  # s
        [None, None, 1, 2, None],  # t
        [None, None, None, None, 4],  # x
        [None, 3, 9, None, 2],  # y
        [7, None, 6, None, None],  # z
    ]

    parents = djikstra(G, 0)
    print(parents)


def dijkstra(G, s):
    queue = PriorityQueue()
    n = len(G)

    parents = [None] * n
    dist = [float("+inf")] * n
    visited = [False] * n

    dist[s] = 0
    queue.put((0, s))

    while not queue.empty():
        _, v_idx = queue.get()

        if visited[v_idx]:
            continue
        visited[v_idx] = True

        for u_idx, w in G[v_idx]:
            if dist[u_idx] > dist[v_idx] + w:
                dist[u_idx] = dist[v_idx] + w
                parents[u_idx] = v_idx
                queue.put((dist[u_idx], u_idx))

    return parents


if __name__ == "__main__":
    G = [[(1, 0), (2, 1)],
         [(3, 1), (2, 0)],
         [(3, 0)],
         []]

    print(dijkstra(G, 0))
