from queue import PriorityQueue


class Node(object):
    def __init__(self):
        self.d = float("+inf")
        self.parent = None
        self.visited = False
        self.rank = 0

    def __repr__(self):
        return f"({self.d} {self.parent is None} {self.visited})"


def make_set(node: Node):
    node.rank = 0
    node.parent = node


def find_set(node: Node):
    if node.parent is not node:
        node.parent = find_set(node.parent)
    return node.parent


def union(u: Node, v: Node):
    link(find_set(u), find_set(v))


def link(u: Node, v: Node):
    if u.rank > v.rank:
        v.parent = u
    else:
        u.parent = v
        if v.rank == u.rank:
            v.rank += 1


def kruskal(G):
    nodes = [Node() for _ in range(len(G))]

    for node in nodes:
        make_set(node)

    queue = PriorityQueue()
    for i in range(len(G)):
        for u_idx in range(len(G)):
            for v_idx in range(len(G)):
                w = G[u_idx][v_idx]

                if w is None:
                    continue

                queue.put((w, u_idx, v_idx))

    edges = []
    while not queue.empty():
        w, u_idx, v_idx = queue.get()
        u, v = nodes[u_idx], nodes[v_idx]

        if find_set(u) is not find_set(v):
            edges.append((u_idx, v_idx))
            union(u, v)

    return edges


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
    print(list(map(lambda a: f"{idx[a[0]]} -- {idx[a[1]]}", kruskal(G))))

