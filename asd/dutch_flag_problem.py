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


def three_way_partition(arr, p, r, pivot_idx, n, key=None):
    key = key if key is not None else (lambda i: arr[i])

    low = p
    mid = p
    high = r

    pivot = key(pivot_idx)

    while mid <= high:
        val = key(mid)

        if val < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif val == pivot:
            mid += 1

        elif val > pivot:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    if n < low:
        return low

    if n <= mid - 1:
        return mid - 1

    return mid - 1


if __name__ == '__main__':
    tab = [3, 3, 3, 1, 0, 4, 5, 6]
    for i in range(len(tab)):
        pivot = tab[i]

        tab_a = tab.copy()
        a = partition_eq(tab_a, 0, len(tab) - 1, i, 300)

        tab_b = tab.copy()
        b = three_way_partition(tab_b, 0, len(tab) - 1, i, 300)

        assert tab_a[a] == tab_b[b]

        tab_a = tab.copy()
        a = partition_eq(tab_a, 0, len(tab) - 1, i, 1)

        tab_b = tab.copy()
        b = three_way_partition(tab_b, 0, len(tab) - 1, i, 1)

        assert tab_a[a] == tab_b[b]
