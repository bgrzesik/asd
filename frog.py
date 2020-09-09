import math


def zbigniew(A):
    n = len(A)

    F = [[math.inf] * n for _ in range(n)]

    F[0][0] = 0

    for i in range(1, n):
        for x in range(n):
            a = math.inf

            if x + 1 < n:
                a = F[i - 1][x + 1]

            if 0 <= x + 1 - A[i - 1] < n:
                a = min(a, F[i - 1][x + 1 - A[i - 1]] + 1)

            F[i][x] = a

    return min(F[-1])
