def count_sort_size(arr):
    buf = [None] * len(arr)
    min_len = min(map(len, arr))
    counts = [0] * (max(map(len, arr)) - min_len + 1)

    for e in arr:
        counts[len(e) - min_len] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    copy = counts.copy()

    for i in range(len(arr) - 1, -1, -1):
        idx = len(arr[i]) - min_len

        buf[counts[idx] - 1] = arr[i]
        counts[idx] -= 1

    arr[:] = buf
    return copy


def count_sort(arr, p, from_):
    def key(e, p):
        if len(e) > p:
            return ord(e[p]) - ord("a")
        else:
            return 0

    buf = [None] * len(arr)
    counts = [0] * 26
    counts[0] = from_

    for i in range(from_, len(arr)):
        counts[key(arr[i], p)] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for i in range(len(arr) - 1, from_ - 1, -1):
        idx = key(arr[i], p)

        buf[counts[idx] - 1] = arr[i]
        counts[idx] -= 1

    for i in range(from_, len(arr)):
        arr[i] = buf[i]

    return arr


def sort_string(arr):
    max_len = max(map(len, arr))

    counts = count_sort_size(arr)

    for i in range(max_len - 1, -1, -1):
        from_ = 0
        if i >= 1:
            from_ = counts[i - 1]

        count_sort(arr, i, from_)

    return arr


if __name__ == "__main__":
    assert count_sort(["a", "d", "a", "d"], 0, 0) == ["a", "a", "d", "d"]

    test = [
        "abc",
        "aaaaa",
        "b",
        "ba",
        "bz",
        "bbb",
        "zaaaaa",
        "bbbba",
        "bz",
        "a",
        "dffgw",
    ]
    assert sort_string(test.copy()) == list(sorted(test))
