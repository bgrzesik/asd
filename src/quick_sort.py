

def partition(arr, p, r, pivot=None):
    if pivot is None:
        pivot = arr[r]

    i = p - 1

    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


if __name__ == '__main__':
    tab = [1, 2, -2, 1, 4, 10, 11, 1, 405]
    quick_sort(tab, 0, len(tab) - 1)
    print(tab)
