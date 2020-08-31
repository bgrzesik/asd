from pprint import pprint
import math


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def shortest(P):
    P.sort(key=lambda e: e[0])
    n = len(P)

    F = [[math.inf] * n for _ in range(n)]

    F[0][0] = 0
    for i in range(1, n):
        F[0][i] = F[0][i-1] + dist(P[i - 1], P[i])

    for i in range(1, n):
        for j in range(i, n):
            m = math.inf
            if i == j or i == j - 1:
                for k in range(i):
                    m = min(m, F[k][i] + dist(P[k], P[j]))
                F[i][j] = m
            else:
                F[i][j] = F[i][j - 1] + dist(P[j - 1], P[j])

    pprint(F)
    return F[n - 1][n - 1]


if __name__ == "__main__":
    P = [(0, 1),
         (1, 0),
         (2, 2),
         (3, 1), ]

    print(shortest(P))
