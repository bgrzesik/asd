from .queue_impl import Queue


class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.fam = None
        self.visited = None

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.fam}, {self.visited}]"


def bfs(G, s):
    queue = Queue()

    for i in range(len(G)):
        v = G[i]
        v.visited = False

    sv = G[s]
    sv.fam = True
    sv.visited = True

    queue.enqueue(s)

    while not queue.is_empty():
        u = queue.dequeue()
        uv = G[u]

        for v in uv.adj:
            vv = G[v]

            if not vv.visited:
                vv.visited = True
                vv.fam = not uv.fam

                queue.enqueue(v)
            elif not (vv.fam ^ uv.fam):  # vv.fam != uv.fam
                return False
    return True


if __name__ == '__main__':
    G = [
        GraphNode([5]),  # 0
        GraphNode([4, 5]),  # 1
        GraphNode([5, 6]),  # 2
        GraphNode([4, 6]),  # 3
        GraphNode([1, 3]),  # 4
        GraphNode([0, 1, 2]),  # 5
        GraphNode([2, 3]),  # 6
    ]
    result = bfs(G, 0)
    print(G, result)
