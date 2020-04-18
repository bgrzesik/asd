from math import ceil

from asd.partition import partition
from asd.quick_select import quick_select_index


def median(arr, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)
    key = key if key is not None else (lambda i: arr[i])

    n = r - p

    if n <= 5:
        return quick_select_index(arr, n // 2 + 1, p, r, key=key)
    else:
        medians = [median(arr, i, min(i + 5, r), key=key) for i in range(p, r, 5)]

        wrapped_idx = median(medians, key=(lambda i: key(medians[i])))

        return medians[wrapped_idx]


if __name__ == '__main__':
    tab = [2, 4, 0, 3, 1]

    assert median(tab) == 2
    assert median([0]) == 0
    assert median([1, 0]) == 0
    assert median([1, 0, 2]) == 1

    assert median([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 7
