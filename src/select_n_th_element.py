from .quick_sort import partition


def _select(arr, p, r, i):
    if p == r:
        return arr[p]

    q = partition(arr, p, r)
    k = q - p + 1

    if k == i:
        return arr[q]
    elif i < k:
        return _select(arr, p, q - 1, i)
    else:
        return _select(arr, q + 1, r, i - k)


def select(arr, i):
    return _select(arr, 0, len(arr) - 1, i)


if __name__ == '__main__':
    tab = [0, 2, 4, 1, 3, 5]
    print(tab, select(tab, 2), list(sorted(tab))[2], list(sorted(tab)))
