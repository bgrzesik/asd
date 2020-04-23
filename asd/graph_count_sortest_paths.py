def count_shortest_paths(G, s, t):
    costs = [float("+inf")] * len(G)
    queue = [s]
    costs[s] = 0

    n = len(G)

    while len(queue) != 0:
        v = queue.pop()

        for u in range(n):
            if not G[v][u]:
                continue

            if costs[u] > costs[v] + 1:
                costs[u] = costs[v] + 1
                queue.insert(0, u)

    count = 0
    queue.insert(0, t)
    while len(queue) != 0:
        v = queue.pop()

        if v == s:
            count += 1
            continue

        for u in range(n):
            if not G[u][v]:
                continue

            if costs[u] == costs[v] - 1:
                queue.insert(0, u)

    return count


G = [[False, True, True, False],
     [False, False, True, True],
     [False, False, False, True],
     [False, False, False, False]]
print(count_shortest_paths(G, 0, 3))

# G = [[False, True, True, True, False],
#      [False, False, True, False, True],
#      [False, False, False, False, True],
#      [False, False, True, False, True],
#      [False, False, False, False, False]]
# print(count_shortest_paths(G, 0, 4))
