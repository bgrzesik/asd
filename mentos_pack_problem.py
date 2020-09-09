import math
from pprint import pprint


def maximize(P):
    n = len(P)

    F = [[None] * n for _ in range(n)]

    def f(i, j):
        print(i, j)

        if i >= j:
            return 0

        if F[i][j] is not None:
            return F[i][j]

        if P[j] > P[i]:
            if P[j - 1] > P[i]:
                F[i][j] = f(i, j - 2) + P[j]
            else:
                F[i][j] = f(i + 1, j - 1) + P[j]
        else:
            if P[i + 1] < P[j]:
                F[i][j] = f(i + 1, j - 1) + P[i]
            else:
                F[i][j] = f(i + 2, j) + P[i]

        return F[i][j]

    r = max(f(0, n - 1), f(1, n - 1), f(0, n - 2))

    pprint(F)

    return r


if __name__ == "__main__":
    P = [9, 11, 7, 5, 4, 6, 8, 10]
    print(maximize(P))
