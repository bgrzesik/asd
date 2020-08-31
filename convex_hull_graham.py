from functools import cmp_to_key, partial
from typing import *
from random import Random


def angle_cmp(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) - \
           (p2[0] - p1[0]) * (p3[1] - p1[1])


def cmp_points(p1, p2):
    if p1[1] - p2[1] != 0:
        return p1[1] - p2[1]
    else:
        return p1[0] - p2[0]


def convex_hull(pl):
    pl.sort(key=cmp_to_key(cmp_points))
    queue = [pl[0]]

    pl = pl[1:]
    pl.sort(key=cmp_to_key(partial(angle_cmp, queue[0])))

    queue.append(pl.pop(0))
    queue.append(pl.pop(0))

    for p in pl:
        while angle_cmp(queue[-2], queue[-1], p) > 0:
            queue.pop()
        queue.append(p)

    return queue


if __name__ == "__main__":
    rand = Random(42)
    pl = [(rand.randrange(1, 100),
           rand.randrange(1, 100)) for _ in range(20)]

    print(convex_hull(pl))

    pl = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]

    print(convex_hull(pl))
