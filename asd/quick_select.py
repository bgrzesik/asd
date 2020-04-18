from asd.partition import partition


def quick_select(arr, i, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)

    if p == r:
        return arr[p]

    q = partition(arr, p, r, key=key)
    k = q - p + 1

    if k == i:
        return arr[q]
    elif i < k:
        return quick_select(arr, i, p, q - 1, key=key)
    else:
        return quick_select(arr, i - k, q + 1, r, key=key)


def quick_select_index(arr, i, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)

    if p == r:
        return p

    q = partition(arr, p, r, key=key)
    k = q - p + 1

    if k == i:
        return q
    elif i < k:
        return quick_select_index(arr, i, p, q - 1, key=key)
    else:
        return quick_select_index(arr, i - k, q + 1, r, key=key)


if __name__ == '__main__':
    tab = [0, 2, 4, 1, 3, 5]

    for i in range(len(tab)):
        assert quick_select(tab, i + 1) == list(sorted(tab))[i]

    for i in range(len(tab)):
        index = quick_select_index(tab, i + 1)
        assert tab[index] == list(sorted(tab))[i]

    print(tab, quick_select(tab, 1), list(sorted(tab))[1 - 1], list(sorted(tab)))
