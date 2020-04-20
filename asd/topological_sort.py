class GraphNode(object):
    def __init__(self, adj: list = None):
        self.adj = adj if adj is not None else []
        self.visited = False

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.visited}]"


def topological_sort(G, start_idx):
    tab = []

    def dfs_visit(v_idx):
        nonlocal G

        v = G[v_idx]
        v.visited = True

        for u_idx in v.adj:
            if not G[u_idx].visited:
                dfs_visit(u_idx)

        tab.insert(0, v_idx)

    dfs_visit(start_idx)

    for i, v in enumerate(G):
        if not v.visited:
            dfs_visit(i)

    return tab


if __name__ == '__main__':
    G = [
        GraphNode([2, 4, 1]),  # 0
        GraphNode([2, 3]),  # 1
        GraphNode([]),  # 2
        GraphNode([6, 5]),  # 3
        GraphNode([3]),  # 4
        GraphNode([]),  # 5
        GraphNode([]),  # 6
    ]
    assert topological_sort(G, 0) == [0, 1, 4, 3, 5, 6, 2]
