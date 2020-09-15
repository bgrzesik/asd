

def best_root(L):
    n = len(L)
    d = [None] * n
    v_max = 0

    def visit(v):
        nonlocal L, d, n, v_max

        for u in L[v]:
            if d[u] is not None:
                continue

            d[u] = d[v] + 1

            if d[u] > d[v_max]:
                v_max = u

            visit(u)

    d[0] = 0
    visit(0)

    d = [None] * n
    v_max2 = v_max

    def visit2(v):
        nonlocal L, d, n, v_max2

        for u in L[v]:
            if d[u] is not None:
                continue

            d[u] = d[v] + 1

            if d[u] > d[v_max2]:
                v_max2 = u

            visit2(u)

    d[v_max] = 0
    visit2(v_max)

    l = d[v_max2] // 2

    for i, e in enumerate(d):
        if e == l:
            return i

    return -1
