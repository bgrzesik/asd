from pprint import pprint


def euler_cycle(G, start_idx):
    tab = []
    n = len(G)
    indices = [-1] * n

    def dfs_visit(v):
        nonlocal G

        if indices[v] == n - 1:
            return

        while indices[v] < n - 1:
            indices[v] += 1
            u = indices[v]

            if G[v][u] == 1 or G[u][v] == 1:
                G[v][u] = 0
                G[u][v] = 0

                dfs_visit(u)

        tab.insert(0, v)

    dfs_visit(start_idx)
    for i in range(len(G)):
        dfs_visit(i)

    return tab


def graph_dict_to_mat(G):
    n = len(G.keys())
    G_mat = [None] * n

    for v, adj in G.items():
        v_idx = ord(v) - ord('a')
        G_mat[v_idx] = [0] * n

        for u in adj:
            u_idx = ord(u) - ord('a')
            G_mat[v_idx][u_idx] = 1

    return G_mat


if __name__ == "__main__":
    #     b ----- c
    #   / | \   / | \
    #  a  |   g   |  d
    #   \ | /   \ | /
    #     c ----- f
    G = {
        'a': ['b', 'e'],
        'b': ['a', 'c', 'g', 'e'],
        'c': ['b', 'd', 'g', 'f'],
        'd': ['c', 'f'],
        'e': ['a', 'f', 'g', 'b'],
        'f': ['d', 'e', 'g', 'c'],
        'g': ['b', 'c', 'f', 'e'],
    }
    G_mat = graph_dict_to_mat(G)
    pprint(G_mat)

    cycle = euler_cycle(G_mat, 0)
    print(cycle)
    cycle = [chr(ord('a') + v) for v in cycle]
    print(cycle)
    # probably I should write more comprehensive test, but I don't have time :C
    assert cycle == ['a', 'b', 'c', 'd', 'f', 'c', 'g', 'b', 'e', 'f', 'g', 'e', 'a']
    assert all(map(lambda adj: 1 not in adj, G_mat))
