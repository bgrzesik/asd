
from .quicksort import partition


def iter_quicksort(arr, p, r):
    stack = [(p, r)]

    while stack:
        p, r = stack.pop()

        if p >= r:
            continue

        q = partition(arr, p, r)

        stack.append((p, q - 1))
        stack.append((q + 1, r))


if __name__ == '__main__':
    tab = [1, 2, -2, 1, 4, 10, 11, 1, 405]
    iter_quicksort(tab, 0, len(tab) - 1)
    print(tab)
