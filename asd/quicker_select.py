from asd.partition import partition
from asd.medians_of_medians import median


def quicker_select_index(arr, i, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)

    if p == r:
        return p

    q = partition(arr, p, r, pivot=median(arr, p, r, key=key))
    k = q - p + 1

    if k == i:
        return q
    elif i < k:
        return quicker_select_index(arr, i, p, q - 1, key=key)
    else:
        return quicker_select_index(arr, i - k, q + 1, r, key=key)


if __name__ == '__main__':

    tab = [29, 18, 32, 34, 3, 28, 19, 33, 30, 36, 26, 9, 10, 35, 5, 8, 11, 15, 20, 37,
           21, 23, 27, 0, 25, 16, 22, 17, 13, 6, 39, 24, 38, 1, 31, 7, 12, 4, 14, 2]

    for i in range(len(tab)):
        assert tab[quicker_select_index(tab, i + 1)] == list(sorted(tab))[i]
