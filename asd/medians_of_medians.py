from math import ceil

from asd.partition import partition
from asd.quick_select import quick_select_index

"""
    Implementation of https://en.wikipedia.org/wiki/Median_of_medians
"""
def quicker_select(arr, i, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)
    key = key if key is not None else (lambda i: arr[i])

    if p == r:
        return p

    q = median(arr, p, r, key=key)
    q = partition_eq(arr, p, r, q, i, key=key)
    k = q - p + 1

    if k == i:
        return q
    elif i < k:
        return quicker_select(arr, i, p, q - 1, key=key)
    else:
        return quicker_select(arr, i - k, q + 1, r, key=key)


def partition_eq(arr, p, r, pivot_idx, n, key=None):
    key = key if key is not None else (lambda i: arr[i])

    pivot = key(pivot_idx)

    arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]

    i = p
    for j in range(p, r):
        if key(j) < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    ieq = i
    for j in range(i, r):
        if key(j) == pivot:
            arr[ieq], arr[j] = arr[j], arr[ieq]
            ieq += 1

    arr[ieq], arr[r] = arr[r], arr[ieq]

    if n < i:
        return i  # nth is smaller then pivot

    if n <= ieq:
        return n  # nth is equal to pivot

    return ieq


def partition5(arr, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)
    key = key if key is not None else (lambda i: arr[i])

    i = p + 1

    while i <= r:
        j = i

        while j > p and key(j - 1) > key(j):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        i += 1

    return (p + r) // 2


def median(arr, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)
    key = key if key is not None else (lambda i: arr[i])

    if r - p < 5:
        return partition5(arr, p, r, key=key)

    for i in range(p, r + 1, 5):
        mid = partition5(arr, i, min(i + 4, r), key)

        idx = p + (i - p) // 5

        arr[mid], arr[idx] = arr[idx], arr[mid]

    # return median(arr, p, p + (r - p + 1) // 5, key=key)

    mid = (r - p) // 10 + p + 1
    end = p + (r - p + 1) // 5

    idx = quicker_select(arr, mid, p, end, key=key)
    return idx


if __name__ == '__main__':
    tab = [2, 4, 0, 3, 1]

    assert median(tab) == 2
    assert median([0]) == 0
    assert median([1, 0]) == 0
    assert median([1, 0, 2]) == 1

    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    m = median(tab)
    assert tab[m] == 3

    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    m = median(tab)
    assert tab[m] == 7

    tab = [29, 18, 32, 34, 3, 28, 19, 33, 30, 36, 26, 9, 10, 35, 5, 8, 11, 15, 20, 37,
           21, 23, 27, 0, 25, 16, 22, 17, 13, 6, 39, 24, 38, 1, 31, 7, 12, 4, 14, 2]

    for i in range(len(tab)):
        assert tab[quicker_select(tab, i + 1)] == list(sorted(tab))[i]
