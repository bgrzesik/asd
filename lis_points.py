

def tower2(A):
    n = len(A)
    nodes = [None] * n

    def construct(i):
        nonlocal n, nodes
        nodes[i] = []

        for j in range(i - 1, -1, -1):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1] and nodes[j] is None:
                construct(j)
                nodes[i].append(j)
                nodes[i].extend(nodes[j])

    for i in range(n - 1, -1, -1):
        if nodes[i] is None:
            construct(i)

    d = [None] * n
    v_max = n - 1

    def visit(v):
        nonlocal nodes, d, n, v_max

        for u in nodes[v]:
            if d[u] is not None:
                continue

            d[u] = d[v] + 1

            if d[u] > d[v_max]:
                v_max = u

            visit(u)

    for i in range(n - 1, -1, -1):
        if d[i] is None:
            d[i] = 0
            visit(i)

    return d[v_max] + 1


def tower(A):
    n = len(A)
    F = [None] * n

    F[0] = 1
    for i in range(1, n):
        F[i] = 1
        for j in range(i):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i], F[j] + 1)

    m = F[0]
    for i in range(1, n):
        m = max(m, F[i])

    return m
