def partition(arr, p, r, pivot=None, key=None):
    key = key if key is not None else (lambda i: arr[i])
    pivot = pivot if pivot is not None else r

    arr[r], arr[pivot] = arr[pivot], arr[r]

    pivot = key(r)

    i = p - 1

    for j in range(p, r):
        if key(j) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1