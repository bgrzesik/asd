from dataclasses import dataclass, field
import math


@dataclass
class FindUnion:
    rank: int = 0
    parent: "FindUnion" = field(init=False, repr=False)

    def __post_init__(self):
        self.parent = self

    def find(self):
        if self.parent is not self:
            self.parent = self.parent.find()
        return self.parent

    def union(self, other: "FindUnion"):
        self = self.find()
        other = other.find()

        if self.rank > other.rank:
            other.parent = self
        else:
            if self.rank == other.rank:
                other.rank += 1
            self.parent = other.parent

    def same_set(self, other):
        return self.find() is other.find()

    def __repr__(self):
        return hex(id(self.find())).upper()


@ dataclass(order=True)
class Highway:
    dist: float = field(default=math.inf, compare=True)

    u: int = None
    v: int = None


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.ceil(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def highway(A):
    n = len(A)

    if n == 2:
        return 0

    edges = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            p1 = A[i]
            p2 = A[j]
            edge = Highway(dist=dist(p1, p2), u=i, v=j)
            edges.append(edge)

    edges.sort()

    find_unions = [FindUnion() for _ in range(n)]
    m = len(edges)

    result = math.inf

    for i in range(m - n + 1):

        for find_union in find_unions:
            find_union.parent = find_union
            find_union.rank = 0

        found = 1
        dmin = math.inf
        dmax = -math.inf

        for j in range(i, m):
            if found >= n:
                result = min(result, dmax - dmin)
                break

            edge = edges[j]
            u = find_unions[edge.u]
            v = find_unions[edge.v]

            if not u.same_set(v):
                u.union(v)
                dmin = min(dmin, edge.dist)
                dmax = max(dmax, edge.dist)
                found += 1

    return result
