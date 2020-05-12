from partition import partition
from quick_select import quick_select


def find_range(arr, p, r, nmin, nmax):
    vmin = quick_select(arr, p, r, nmin)
    vmax = quick_select(arr, p, r, nmax)

    q1 = partition(arr, p, r, pivot=vmin)
    print(arr, vmin, q1)

    q2 = partition(arr, q1, r, pivot=vmax)
    print(arr, vmax, q2)

    print(vmin, vmax, q1, q2)

    return arr[q1 - 1:q2 + 1]


if __name__ == "__main__":
    tab = [0, 2, 4, 1, 3, 5]
    find_range(tab, 0, len(tab) - 1, 2, 4), tab, list(sorted([0, 2, 4, 1, 3, 5]))
