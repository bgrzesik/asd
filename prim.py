from queue import PriorityQueue

# O(E log V)


class Node(object):
    def __init__(self):
        self.parent = None
        self.visited = False
        self.key = float("+inf")


def prim(G, r):
    nodes = [Node() for _ in range(len(G))]

    Q = PriorityQueue()
    Q.put((0, r))
    nodes[r].key = 0

    while not Q.empty():
        _, v = Q.get()

        if nodes[v].visited:
            continue

        nodes[v].visited = True

        for u, w in enumerate(G[v]):
            if w is None:
                continue

            if not nodes[u].visited and w < nodes[u].key:
                nodes[u].parent = v
                nodes[u].key = w
                Q.put((w, u))
    mst = [(v, node.parent)
           for v, node in enumerate(nodes)
           if node.parent is not None]

    cost = sum([G[v][u] for v, u in mst])

    return mst, cost


if __name__ == "__main__":
    G = [[None, 4, None, None, None, None, None, 8, None],
         [4, None, 8, None, None, None, None, 11, None],
         [None, 8, None, 7, None, 4, None, None, 2],
         [None, None, 7, None, 9, 14, None, None, None],
         [None, None, None, 9, None, 10, None, None, None],
         [None, None, 4, 14, 10, None, 2, None, None],
         [None, None, None, None, None, 2, None, 1, 6],
         [8, 11, None, None, None, None, 1, None, 7],
         [None, None, 2, None, None, None, 6, 7, None]]
    idx = "abcdefghi"

    mst, cost = prim(G, 0)
    mst = [f"{idx[u]} -- {idx[v]}" for u, v in mst]
    mst.sort()
    print(mst, cost)
