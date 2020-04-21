

from asd.partition import partition


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


if __name__ == "__main__":
    tab = [1, 2, -2, 1, 4, 10, 11, 1, 405]
    quick_sort(tab, 0, len(tab) - 1)
    print(tab)
