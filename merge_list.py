
def _left(idx):
    return 2 * idx + 1


def _right(idx):
    return 2 * idx + 2


def _parent(idx):
    return (idx - 1) // 2


def heap_add(arr, val):
    idx = len(arr)
    arr.append(val)

    while idx > 0 and arr[idx].val < arr[_parent(idx)].val:
        arr[idx], arr[_parent(idx)] = arr[_parent(idx)], arr[idx]
        idx = _parent(idx)


def heapify(arr, idx):
    bigger = idx

    if _right(idx) < len(arr) and arr[_right(idx)].val < arr[bigger].val:
        bigger = _right(idx)

    if _left(idx) < len(arr) and arr[_left(idx)].val < arr[bigger].val:
        bigger = _left(idx)

    if bigger != idx:
        arr[idx], arr[bigger] = arr[bigger], arr[idx]
        heapify(arr, bigger)


def heap_pop(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    val = arr.pop()
    heapify(arr, 0)
    return val


def tasks(T):

    queue = []

    for li in T:
        heap_add(queue, li)

    head = None
    curr = None
    while len(queue) != 0:
        node = queue[0]

        if node.next is not None:
            queue[0] = node.next
            heapify(queue, 0)
        else:
            heap_pop(queue)

        node.next = None
        if head is None:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node

    return head
