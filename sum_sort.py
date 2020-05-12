def sum_sort(A, B, n):
    sums = [0] * n

    for i in range(n):
        for j in range(n):
            sums[i] += A[i * n + j]

    min1 = min(sums)
    max1 = max(sums)
    idx = [0] * (max1 - min1 + 1)

    for s in sums:
        idx[s - min1] += 1

    for i in range(1, len(idx)):
        idx[i] += idx[i - 1]

    for i in range(n - 1, -1, -1):
        dest = idx[sums[i] - min1] - 1
        idx[sums[i] - min1] -= 1

        for j in range(n):
            B[dest * n + j] = A[i * n + j]

    return B


if __name__ == "__main__":
    A = [
        4, 5, 6,
        1, 2, 3,
        7, 8, 9,
    ]
    B = [0] * 3 ** 2
    sum_sort(A, B, 3)
    assert B == [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
    ]

    A = [
        13, 14, 15, 16,
        9, 10, 11, 12,
        1, 2, 3, 4,
        5, 6, 7, 8,
    ]
    B = [0] * 4 ** 2
    sum_sort(A, B, 4)
    assert B == [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 16,
    ]
