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


def articulation_points(G, start_idx):
    visit = 0
    points = set()

    def bfs_visit(v_idx, root):
        nonlocal G, visit, points

        visit += 1

        v = G[v_idx]
        v.visited = True
        v.d = visit
        v.low = v.d

        articulation = False
        children = 0

        for u_idx in v.adj:
            u = G[u_idx]

            if not u.visited:
                u.parent = v_idx
                bfs_visit(u_idx, False)
                v.low = min(v.low, u.low)

                if not root:
                    articulation = articulation or u.low >= v.d

                children += 1
            elif u_idx != v.parent:
                v.low = min(v.low, u.low)

        if articulation or (root and children > 1):
            points.add(v_idx)

    bfs_visit(start_idx, True)
    for i, v in enumerate(G):
        if not v.visited:
            # different connected compound
            bfs_visit(i, True)

    return points


if __name__ == '__main__':
    #   b        e
    #  / \      /|
    #  a  c -- d |
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

    points = articulation_points(G, 0)
    print(points)
    print([chr(ord('a') + v) for v in points])
    pprint(G)
