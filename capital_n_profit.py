

def maximize(C, P, W, k):
    n = len(C)
    U = [None] * n

    O = []

    for i in range(k):
        c = 0

        for j in range(1, n):
            if C[j] <= W and (C[c] > W or P[c] < P[j]) and U[j] is None:
                c = j

        if C[c] > W:
            return None

        U[c] = i
        W += P[c]

    return U, W


if __name__ == "__main__":
    C = [0, 1, 1]
    P = [1, 2, 3]
    k = 2
    W = 0

    print(maximize(C, P, W, k))
