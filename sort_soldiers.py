def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def select(arr, i, p, r):
    if p == r:
        return p

    q = partition(arr, p, r)
    k = q - p + 1

    if k == i:
        return q
    elif i < k:
        return select(arr, i, p, q - 1)
    else:
        return select(arr, i - k, q + 1, r)


def section(T, p, q):
    buf = [None] * (q - p + 1)

    start = select(T, p, 0, len(T) - 1)
    end = select(T, q - start, start, len(T) - 1)

    for i in range(start, end + 1):
        buf[i - p] = T[i]

    return buf


if __name__ == "__main__":
    t = [1, 9, 0, 7, 6, 5, 12, 3, 4, 2, 11, 34]
    print(section(t, 3, 7))
