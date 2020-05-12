from math import log, ceil


def fix_table(arr):
    swaps = ceil(log(len(arr)))
    idx = [-1] * swaps

    found = 0

    for i in range(len(arr)):
        l = float("-inf")
        if i > 0:
            l = arr[i - 1]

        r = float("+inf")
        if i < len(arr) - 1:
            r = arr[i + 1]

        if not (l < arr[i] < r) and l < r:
            idx[found] = i
            found += 1

    for i in range(1, len(idx)):
        val = arr[idx[i]]

        j = i - 1

        while j >= 0 and arr[idx[j]] > val:
            arr[idx[j + 1]] = arr[idx[j]]
            j -= 1

        arr[idx[j + 1]] = val

    return arr


if __name__ == "__main__":
    test = [169, 2698, 932, 1567, 1780,
            2010, 2374, 2583, 688, 3496,
            4075, 4136, 4161, 4520, 5212,
            5513, 6136, 6192, 6298, 9637,
            8640, 8789, 9057, 9081, 8540]
    result = fix_table(test.copy())
    expected = list(sorted(test))
    assert result == expected

    test = [461, 1992, 2025, 2630, 2880,
            3037, 3729, 7881, 4583, 4873,
            5349, 5504, 5855, 6880, 7289,
            7333, 7851, 7871, 4008, 7950,
            9755, 9017, 9156, 9392, 8506]
    result = fix_table(test.copy())
    expected = list(sorted(test))
    assert result == expected
