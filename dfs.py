from pprint import pprint

class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.parent = None
        self.visited = None
        self.entry = None
        self.process = None

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.parent}, {self.visited}, {self.entry}, {self.process}]"


def dfs(G, s):
    time = 0

    def visit(u):
        nonlocal time
        time += 1

        G[u].visited = True
        G[u].entry = time

        for v in G[u].adj:
            if not G[v].visited:
                G[v].parent = u
                visit(v)

        time += 1
        G[u].process = time

    for v in G:
        v.visited = False
        v.parent = None
        v.entry = None
        v.process = None

    visit(s)
    for v in range(len(G)):
        if not G[v].visited:
            visit(v)


if __name__ == "__main__":
    G = [
        GraphNode([1, 2, 3]),  # 0
        GraphNode([0, 4]),  # 1
        GraphNode([0, 4, 5]),  # 2
        GraphNode([0, 5, 4]),  # 3
        GraphNode([1, 2, 3]),  # 4
        GraphNode([2, 3]),  # 5
    ]
    dfs(G, 0)

    assert all(map(lambda v: v.visited, G))
    pprint(G)
