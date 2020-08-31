from functools import cmp_to_key, partial
from typing import *
from random import Random


def two_closest_idotic(pl):
    a = 0
    b = 1
    m = (pl[a][0] - pl[b][0]) ** 2 + (pl[a][1] - pl[b][1]) ** 2
    for i in range(len(pl) - 1):
        for j in range(i + 1, len(pl)):
            d = (pl[i][0] - pl[j][0]) ** 2 + (pl[i][1] - pl[j][1]) ** 2
            if m > d:
                a = i
                b = j
                m = d
    return m


def _two_closest2(pl, d):
    m = d
    pl.sort(key=lambda p: p[1])

    for i in range(len(pl) - 1):
        for j in range(i + 1, len(pl)):
            d = (pl[i][0] - pl[j][0]) ** 2 + (pl[i][1] - pl[j][1]) ** 2
            if m > d:
                m = d

    return m


def _two_closest(pl):
    if len(pl) <= 3:
        return two_closest_idotic(pl)

    mid = len(pl) // 2

    dl = _two_closest(pl[mid:])
    dr = _two_closest(pl[:mid])
    d = min(dl, dr)

    strip = []
    for p in pl:
        if abs(p[0] - pl[mid][0]) < d:
            strip.append(p)
    return min(d, _two_closest2(strip, d))


def two_closest(pl):
    pl.sort(key=lambda p: p[0])
    return _two_closest(pl)


if __name__ == "__main__":
    rand = Random(42)
    pl = [(rand.randrange(1, 100),
           rand.randrange(1, 100)) for _ in range(20)]

    print(two_closest_idotic(pl))
    print(two_closest(pl))
