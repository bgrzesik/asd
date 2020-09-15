from functools import cmp_to_key, partial
from typing import *
from random import Random

# O(n * h)

def angle_cmp(p1, p2, p3):

    return (p3[0] - p1[0]) * (p2[1] - p1[1])\
        - (p2[0] - p1[0]) * (p3[1] - p1[1])


def cmp_points(p1, p2):
    if p1[1] - p2[1] != 0:
        return p1[1] - p2[1]
    else:
        return p1[0] - p2[0]


def convex_hull(pl):
    start = min(pl, key=lambda p: p[0])
    w = []

    f = None
    p = start
    while f is not start:
        ff = pl[0] if pl[0] is not p else pl[1]
        f = ff
        for pp in pl:
            if angle_cmp(p, f, pp) > 0:
                f = pp

        w.append(f)
        p = f

    return w


if __name__ == "__main__":
    rand = Random(42)
    pl = [(rand.randrange(1, 100),
           rand.randrange(1, 100)) for _ in range(20)]

    print(convex_hull(pl))

    pl = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]

    print(convex_hull(pl))
