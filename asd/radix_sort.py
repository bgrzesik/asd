from math import log10, floor


def count_sort10(arr, pow10):
    buf = [None] * len(arr)
    counts = [0] * len(arr)

    for e in arr:
        e = floor(e / pow10) % 10
        counts[e] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        idx = floor(arr[i] / pow10) % 10

        buf[counts[idx] - 1] = arr[i]
        counts[idx] -= 1

    arr[:] = buf
    return arr


def radix_sort(arr):
    mul = 1

    n = floor(log10(max(arr)))

    for i in range(n + 1):
        count_sort10(arr, mul)
        mul *= 10

    return arr


if __name__ == '__main__':
    l = [0, 9, 2, 3, 5, 5, 7, 8, 4, 6]
    arr = count_sort10(l, 1)
    assert list(sorted(l.copy())) == arr

    l = [0, 90, 20, 30, 50, 50, 70, 80, 40, 60]
    arr = count_sort10(l.copy(), 10)
    assert list(sorted(l)) == arr
    l = [666, 777, 888, 112, 123, 112, 8, 10, 0, 1002]
    arr = radix_sort(l.copy())
    assert list(sorted(l)) == arr
