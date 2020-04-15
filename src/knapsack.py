def knapsack(W, P, max_w):
    n = len(W)
    F = [None] * n

    for i in range(n):
        F[i] = [0] * (max_w + 1)

    for w in range(W[0], max_w + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = F[i - 1][w]

            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])

    return F[n - 1][max_w]


if __name__ == "__main__":
    W = [4, 1, 2, 4, 3, 5, 10, 3]
    P = [7, 3, 2, 10, 4, 1, 7, 2]

    knapsack(W, P, 11)


def knapsack(W, P, max_w):
    n = len(W)
    F = [[0] * (max_w + 1) for i in range(n)]

    # używam zagnieżdżonych funkcji aby uniknąć używania zmieninych globalnych
    def f(i, w):
        val = 0

        if F[i][w] != 0:
            return F[i][w]
        elif (i == 0 and w < W[0]) or w == 0:
            val = 0
        elif i == 0:
            val = P[0]
        else:
            val = f(i - 1, w)
            if w >= W[i]:
                val = max(val, f(i - 1, w - W[i])  + P[i])

        F[i][w] = val

        return val

    return f(n - 1, max_w)

if __name__ == "__main__":
    W = [4, 1, 2, 4, 3, 5, 10, 3]
    P = [7, 3, 2, 10, 4, 1, 7, 2]

    knapsack(W, P, 11)


def knapsack(W, P, max_w):
    n = len(W)
    F = [[0] * (max_w + 1) for i in range(n)]
    N = [[(-1, -1)] * (max_w + 1) for i in range(n)] # tablica przechowująca "x i y" poprzedniego elementu z F

    for w in range(W[0], max_w + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = F[i - 1][w]
            N[i][w] = (i - 1, w)

            if w >= W[i]:
                profit = F[i - 1][w - W[i]] + P[i]
                if F[i][w] < profit:
                    F[i][w] = profit
                    N[i][w] = (i - 1, w - W[i])

    items = []
    i, w = N[n - 1][max_w]

    while i != -1:
        ni, nw = N[i][w]
        if nw != w and w != -1:
            items.append(i) # wybieram tylko indeksy po których nastąpiła "zmiana wagi plecaka"
        i, w = ni, nw

    return F[n - 1][max_w], items


if __name__ == "__main__":
    W = [4, 1, 2, 4, 3, 5, 10, 3]
    P = [7, 3, 2, 10, 4, 1, 7, 2]

    knapsack(W, P, 11)
