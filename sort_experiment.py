import math


def partition(tab, lo, hi):
    i = lo - 1
    for j in range(lo, hi):
        if tab[j] <= tab[hi]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    i += 1
    tab[i], tab[hi] = tab[hi], tab[i]

    return i


def qsort(tab, lo, hi):
    if lo >= hi:
        return

    p = partition(tab, lo, hi)
    qsort(tab, lo, p - 1)
    qsort(tab, p + 1, hi)


def fast_sort(tab, a):
    n = len(tab)

    buckets = [[] for _ in range(n)]

    loga = math.log(a)

    for e in tab:
        x = math.log(e) / loga
        buckets[int(x * n)].append(e)

    for bucket in buckets:
        qsort(bucket, 0, len(bucket) - 1)

    i = 0
    for bucket in buckets:
        for e in bucket:
            tab[i] = e
            i += 1

    return tab
