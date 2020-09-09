

def partition(arr, lo, hi):
    pivot = arr[hi]

    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]

    return i

def quick_sort(arr, lo, hi):

    while lo < hi:
        pi = partition(arr, lo, hi)

        if (pi - lo + 1) > (hi - pi + 1):
            quick_sort(arr, lo, pi - 1)
            lo, hi = pi + 1, hi
        else:
            quick_sort(arr, pi + 1, hi)
            lo, hi = lo, pi - 1


def rev_quick_sort(arr, lo, hi):
    for i in range(len(arr)):
        arr[i] = -arr[i]

    quick_sort(arr, lo, hi)

    for i in range(len(arr)):
        arr[i] = -arr[i]


if __name__ == "__main__":
    arr = [9, 1, 23, 2, 10, 4, 8]

    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [9, 1, 23, 2, 10, 4, 8]

    rev_quick_sort(arr, 0, len(arr) - 1)
    print(arr)
