from pprint import pprint


def floyd_warshall(W):
    S = [w.copy() for w in W]
    P = [[None] * len(w) for w in W]
    n = len(W)

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][j] is None:
                    S[i][j] = float("+inf")

                if S[i][j] > S[i][t] + S[t][j]:
                    S[i][j] = S[i][t] + S[t][j]
                    P[i][j] = t

    return S, P


def get_path(S, P, s, t):
    path = []
    tt = t
    while t is not None:
        path.insert(0, t)
        t = P[s][t]
        if t is None:
            path.insert(0, s)

    return path, S[s][tt]

if __name__ == "__main__":
    names = "stxyz"
    G = [
        # s   t   x   y   z
        [None, 10, None, 5, None],  # s
        [None, None, 1, 2, None],  # t
        [None, None, None, None, 4],  # x
        [None, 3, 9, None, 2],  # y
        [7, None, 6, None, None],  # z
    ]

    S, P = floyd_warshall(G)

    pprint(S)
    pprint(P)

    pprint(S[0][4])

    pprint(get_path(S, P, 0, 4))
