from asd.dutch_flag_problem import three_way_partition


# Implementation of https://en.wikipedia.org/wiki/Median_of_medians
def quicker_select(arr, i, p=None, r=None, key=None):
    p = p if p is not None else 0
    r = r if r is not None else (len(arr) - 1)
    key = key if key is not None else (lambda i: arr[i])

    if p == r:
        return p

    q = median(arr, p, r, key=key)
    q = three_way_partition(arr, p, r, q, i, key=key)
    k = q - p + 1

    if k == i:
        return q
    elif i < k:
        return quicker_select(arr, i, p, q - 1, key=key)
    else:
        return quicker_select(arr, i - k, q + 1, r, key=key)


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


def _select_partition(arr, left, right):
    # arr[r], arr[pivot] = arr[pivot], arr[r]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= arr[right]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def _select_insert_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        val = arr[i]
        j = i - 1

        while j >= 0 and arr[j] >= val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = val


def select(arr, left, right, i):
    n = right - left + 1

    if n < 5:
        _select_insert_sort(arr, left, right)
        return left + i - 1

    slow = left
    for l in range(left, right, 5):
        r = min(l + 4, right)

        if r - l < 3:
            continue

        _select_insert_sort(arr, l, r)

        mid = (l + r) // 2

        print(f"median {arr[mid]}")

        arr[slow], arr[mid] = arr[mid], arr[slow]

        slow += 1
    print(f"====")

    med = select(arr, left, slow - 1, (slow - left + 1) // 2)

    arr[med], arr[right] = arr[right], arr[med]
    mid = _select_partition(arr, left, right)

    k = mid - left + 1

    if k == i:
        return mid
    elif k > i:
        return select(arr, left, mid - 1, i)
    else:
        return select(arr, mid + 1, right, i - k)


if __name__ == "__main__":
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

    assert select([4, 3, 2, 1, 0], 0, 4, 2) == 1
    tab = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
    assert tab[select(tab, 0, 9, 4)] == 1
    tab = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 2, 2]
    assert tab[select(tab, 0, 11, 5)] == 2
    tab = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert tab[select(tab, 0, 11, 4)] == 3

