from asd.queue_impl import Queue


class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.d = None
        self.visited = None
        self.parent = None

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.d}, {self.visited}, {self.parent}]"


def bfs(G, s):
    queue = Queue()

    for i in range(len(G)):
        v = G[i]
        v.visited = False

    sv = G[s]
    sv.d = 0
    sv.visited = True
    sv.parent = None

    queue.enqueue(s)

    while not queue.is_empty():
        u = queue.dequeue()
        uv = G[u]

        for v in uv.adj:
            vv = G[v]

            if not vv.visited:
                vv.visited = True
                vv.d = uv.d + 1
                vv.parent = u

                queue.enqueue(v)


if __name__ == '__main__':
    G = [
        GraphNode([1, 2, 3]),  # 0
        GraphNode([0, 4]),  # 1
        GraphNode([0, 4, 5]),  # 2
        GraphNode([0, 5, 4]),  # 3
        GraphNode([1, 2, 3]),  # 4
        GraphNode([2, 3]),  # 5
    ]
    bfs(G, 0)
    print(G)
