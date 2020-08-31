
from graph_util import unmat_to_dot
import math


def stations(G, P, D, s, t):
    n = len(G)

    # F = [[[[math.inf] * (D + 1) for _ in range(n)]] for _ in range(n)]
    # T = [[[[0] * (D + 1) for _ in range(n)]] for _ in range(n)]
    F = [[math.inf] * (D + 1) for _ in range(n)]
    PP = [[None] * (D + 1) for _ in range(n)]
    BB = [[None] * (D + 1) for _ in range(n)]

    F[s] = [0] * (D + 1)

    for _ in range(n):
        for u in range(n):
            for v in range(n):
                for p1 in range(D + 1):
                    for p2 in range(D + 1):
                        if not (p2 + G[u][v] <= D):
                            continue  # not overfilling the tank

                        buy = (p2 + G[u][v]) - p1
                        if buy < 0:
                            continue  # we are not selling the fuel

                        cost = F[u][p1] + buy * P[u]
                        if F[v][p2] > cost:
                            F[v][p2] = cost
                            PP[v][p2] = u
                            BB[v][p2] = p1

    a = t
    p2 = 0
    while PP[a][p2] is not None:
        p = PP[a][p2]
        p1 = BB[a][p2]

        print(f"{a} <- {p}")
        print(f"distance {G[p][a]}")
        print(f"on {p} was {p1}")
        print(f"on {a} was {p2} (current)")
        print(f"buy {(p2 + G[p][a]) - p1}")
        print(f"cost (so far) {F[a][p2]}")
        print()

        p2 = BB[a][p2]
        a = p

    return F[t][0]


if __name__ == "__main__":
    G = [
        [0, 70, 0, 0, 0, 0, 30, 50],
        [70, 0, 0, 40, 0, 0, 0, 10],
        [0, 0, 0, 30, 20, 0, 20, 0],
        [0, 40, 30, 0, 5, 10, 0, 0],
        [0, 0, 20, 5, 0, 30, 0, 0],
        [0, 0, 0, 10, 30, 0, 0, 0],
        [30, 0, 20, 0, 0, 0, 0, 0],
        [50, 10, 0, 0, 0, 0, 0, 0],
    ]
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] == 0:
                G[u][v] = math.inf
    P = [0, 40, 50, 10, 100, 0, 20, 100]

    print(unmat_to_dot(G,
                       vex_info=lambda v: f'label="{v}: {P[v]} zl/l"',
                       edge_exists=lambda e: e != math.inf,
                       edge_info=lambda u, v, e: f'label="{e}"'))

    print(stations(G, P, 70, 0, 5))
