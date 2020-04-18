def lis_dyn(A):
    B = [float("-inf")] * len(A)
    C = [None] * len(A)

    B[0] = 1
    C[0] = None

    for i in range(1, len(B)):
        for j in range(i - 1, -1, -1):
            if A[i] > A[j]:
                if B[i] < B[j] + 1:
                    B[i] = B[j] + 1
                    C[i] = j

    m = 0
    for i in range(1, len(B)):
        if B[m] < B[i]:
            m = i

    p = m
    arr = []
    while p is not None:
        arr.insert(0, A[p])
        p = C[p]

    return B[m], arr


if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    assert lis_dyn(arr) == (6, [0, 2, 6, 9, 11, 15])
