from asd.minmax_heap import Heap


def find_smallest_range(arrays):
    heap = Heap(key=lambda e: e[0])

    n = len(arrays)
    k = len(arrays[0])

    for i in range(n):
        heap.insert((arrays[i][0], i, 0))

    r_min, _, _ = heap.peek_min()
    r_max, _, _ = heap.peek_max()

    while not heap.is_empty():
        min_val, min_arr, min_idx = heap.peek_min()
        max_val, _, _ = heap.peek_max()

        if (r_max - r_min) > (max_val - min_val):
            r_max = max_val
            r_min = min_val

        min_idx += 1
        if min_idx >= k:
            break

        min_val = arrays[min_arr][min_idx]

        heap.arr[0] = (min_val, min_arr, min_idx)
        heap.push_down(0)

    return r_min, r_max


if __name__ == "__main__":
    arrays = [
        [4, 7, 9, 12, 15],
        [0, 8, 10, 14, 20],
        [6, 12, 16, 30, 50],
    ]

    assert find_smallest_range(arrays) == (6, 8)

    arrays = [
        [4, 7],
        [1, 2],
        [20, 40]
    ]

    assert find_smallest_range(arrays) == (2, 20)
