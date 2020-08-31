
def _left(idx):
    return 2 * idx + 1


def _right(idx):
    return 2 * idx + 2


def _parent(idx):
    return (idx - 1) // 2


def heapify_down(arr, idx, key=lambda e: e):
    bigger = idx

    if _right(idx) < len(arr) and key(arr[_right(idx)]) > key(arr[bigger]):
        bigger = _right(idx)

    if _left(idx) < len(arr) and key(arr[_left(idx)]) > key(arr[bigger]):
        bigger = _left(idx)

    if bigger != idx:
        arr[idx], arr[bigger] = arr[bigger], arr[idx]
        heapify_down(arr, bigger)


def heapify_up(arr, idx, key=lambda e: e):
    while idx > 0 and key(arr[idx]) > key(arr[_parent(idx)]):
        arr[idx], arr[_parent(idx)] = arr[_parent(idx)], arr[idx]
        idx = _parent(idx)


def heap_add(arr, val, key=lambda e: e):
    idx = len(arr)
    arr.append(val)
    heapify_up(arr, idx, key=key)


def heap_peak(arr):
    return arr[0]


def heap_pop(arr, key=lambda e: e):
    arr[0], arr[-1] = arr[-1], arr[0]
    val = arr.pop()
    heapify_down(arr, 0, key=key)
    return val


def heapify_all(arr):
    for i in range(len(arr) // 2 + 1, 0, -1):
        heapify_down(arr, i)


if __name__ == "__main__":
    a = list(range(10))

    heapify_all(a)
    print(a)
    while a:
        print(heap_pop(a))
