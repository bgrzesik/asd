def path_cost(G, s, t):
    costs = [float("+inf")] * len(G)
    queue0 = [s]
    queue1 = []

    costs[s] = 0

    while len(queue0) != 0 or len(queue1) != 0:
        v = None
        if len(queue0) != 0:
            v = queue0.pop()
        else:
            v = queue1.pop()

        for u, c in G[v]:
            if costs[u] > costs[v] + c:
                costs[u] = costs[v] + c

                if c == 0:
                    queue0.insert(0, u)
                else:
                    queue1.insert(0, u)
    print(costs)
    return costs[t]


G = [[(1, 0), (2, 1)],
     [(3, 1), (2, 0)],
     [(3, 0)],
     []]

print(path_cost(G, 0, 3))

# G = [[(1, 0), (5, 0)],
#      [(3, 1), (2, 1)],
#      [],
#      [(2, 0), (5, 1)],
#      [(0, 1), (3, 1)],
#      [(4, 1)]]
#
# print(path_cost(G, 0, 2))
