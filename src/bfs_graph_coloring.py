from .queue_impl import Queue

from pprint import pprint
from math import log2, floor, ceil


class GraphNode:
    def __init__(self, adj=None):
        self.adj = adj if adj is not None else []
        self.color = None
        self.visited = None

    def __repr__(self):
        return f"GraphNode[{self.adj}, {self.color}, {self.visited}]"


def least_significant_nonzero_bit32(a):
    a |= a << 32
    a |= a << 16
    a |= a << 8
    a |= a << 4
    a |= a << 2
    a |= a << 1
    return a ^ (a << 1)


def first_zerobit(a):
    a = least_significant_nonzero_bit32(~a)
    return floor(log2(a))


def bfs_color(G, s=0):
    WHITE = 0
    GREY = 1
    BLACK = 2

    queue = Queue()

    for v in G:
        v.visited = WHITE

    # heurystyka
    if s is None:
        s = max(max(G, key=lambda v: len(v.adj)).adj)

    sv = G[s]
    sv.color = first_zerobit(0)
    sv.visited = GREY

    queue.enqueue(s)

    while not queue.is_empty():
        u = queue.dequeue()
        uv = G[u]

        mask = 0

        for v in uv.adj:
            vv = G[v]

            if vv.visited == WHITE:
                vv.visited = GREY
                queue.enqueue(v)
            elif vv.visited == BLACK:
                mask |= 1 << vv.color

        uv.visited = BLACK
        uv.color = first_zerobit(mask)


def complete_graph(n):
    verts = []
    adjs = list(range(n))
    for i in range(n):
        verts.append(GraphNode([j for j in range(n) if j != i]))
    return verts


G = [
    GraphNode([5]),  # 0
    GraphNode([4, 5]),  # 1
    GraphNode([5, 6]),  # 2
    GraphNode([4, 6]),  # 3
    GraphNode([1, 3]),  # 4
    GraphNode([0, 1, 2]),  # 5
    GraphNode([2, 3]),  # 6
]

PERTERSEN = [
    GraphNode([1, 4, 6]),  # 0
    GraphNode([0, 2, 7]),  # 1
    GraphNode([1, 3, 8]),  # 2
    GraphNode([2, 4, 9]),  # 3
    GraphNode([0, 3, 5]),  # 4
    GraphNode([4, 6, 9]),  # 5
    GraphNode([0, 5, 7]),  # 6
    GraphNode([1, 6, 8]),  # 7
    GraphNode([2, 7, 9]),  # 8
    GraphNode([3, 8, 5]),  # 9
]

if __name__ == '__main__':
    bfs_color(G)
    bfs_color(PERTERSEN)

    pprint(list(enumerate(G)))
    pprint(set(map(lambda v: v.color, G)))
    pprint(list(enumerate(PERTERSEN)))
    pprint(set(map(lambda v: v.color, PERTERSEN)))

    for n in range(3, 30):
        KN = complete_graph(n)
        bfs_color(KN)
        assert len(set(map(lambda v: v.color, KN))) == n


dataset = [
    ("queen11_11.col", 11),
    ("queen13_13.col", 13),
    ("queen5_5.col", 5),
    ("queen6_6.col", 7),
    ("queen7_7.col", 7),
    ("queen8_12.col", 12),
    ("queen8_8.col", 9),
    ("queen9_9.col", 10),
]


def read_graph(filename):
    import urllib.request

    lines = data = urllib.request.urlopen(f"https://mat.tepper.cmu.edu/COLOR/instances/{filename}")
    verts = []

    for line in lines:
        line = line.decode('utf-8')
        line = line.split(" ")
        if line[0] == "c":
            continue
        elif line[0] == "p":
            verts = [GraphNode([]) for i in range(int(line[2]))]
        elif line[0] == "e":
            u = int(line[1]) - 1
            v = int(line[2]) - 1
            verts[u].adj.append(v)
    return verts


if __name__ == '__main__':
    for file, colors in dataset:
        G = read_graph(file)
        min_colors = 2000

        for i in range(len(G)):
            bfs_color(G, s=i)
            min_colors = min(min_colors, len(set(map(lambda v: v.color, G))))

        print(min_colors, colors)
