from pprint import pprint


class GraphNode(object):
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.visited = False
        self.parent = None
        self.low = None
        self.d = None

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.visited}, {self.low}, {self.d}, {self.parent}]"


def bridges(G, start_idx):
    visit = 0
    bridges = []

    def bfs_visit(v_idx):
        nonlocal G, visit, bridges

        visit += 1

        v = G[v_idx]
        v.visited = True
        v.d = visit
        v.low = v.d

        for u_idx in v.adj:
            u = G[u_idx]

            if not u.visited:
                u.parent = v_idx
                bfs_visit(u_idx)
                v.low = min(v.low, u.low)
            elif u_idx != v.parent:
                v.low = min(v.low, u.low)

        if v.d == v.low and v.parent is not None:
            bridges.append((v.parent, v_idx))

    bfs_visit(start_idx)
    for i, v in enumerate(G):
        if not v.visited:
            bfs_visit(i)

    return bridges


if __name__ == "__main__":
    #   b        e
    #  / \      /|
    #  a  c -- b |
    #  \ /      \|
    #   g        f
    #   |
    #   h

    G = [
        GraphNode([1, 6]),  # 0 a
        GraphNode([0, 2]),  # 1 b
        GraphNode([1, 3, 6]),  # 2 c
        GraphNode([2, 4, 5]),  # 3 d
        GraphNode([3, 5]),  # 4 e
        GraphNode([3, 4]),  # 5 f
        GraphNode([0, 2, 7]),  # 6 g
        GraphNode([6]),  # 7 h
    ]

    print(bridges(G, 0))
    pprint(G)

