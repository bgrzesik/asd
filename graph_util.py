from functools import partial


def identity(e, *arg):
    return e


def _format(a, end):
    if type(a) != dict:
        return a

    s = ""
    for key, val in a.items():
        val = _format(val, "\\n")
        if end != "\\n":
            val = f'"{val}"'
        s += f"{key}={val}{end}"
    return s


def adj_to_dot(G,
               vex_to_idx=identity,
               vex_info=partial(identity, ""),
               vex_to_adj=identity,
               edge_to_idx=identity,
               edge_info=partial(identity, "")):

    dot = "digraph {\n"

    for i, adj in enumerate(G):
        idx = vex_to_idx(i, adj)
        adj_list = vex_to_adj(adj)

        dot += f"\t{idx} [{_format(vex_info(i, adj), ',')}]\n"

        for _j, a in enumerate(adj_list):
            idx2 = edge_to_idx(a)
            info = _format(edge_info(i, a), ",")

            dot += f"\t{idx} -> {idx2} [{info}]\n"

    dot += "}\n"

    return dot


def mat_to_dot(G,
               vex_info=partial(identity, ""),
               edge_exists=lambda e: e is not None,
               edge_info=partial(identity, "")):

    dot = "digraph {\n"
    for vidx in range(len(G)):
        info = _format(vex_info(vidx), ",")
        dot += f'\t{vidx} [{info}]\n'
        for uidx in range(len(G)):
            e = G[vidx][uidx]
            if edge_exists(e):
                info = _format(edge_info(vidx, uidx, e), ",")
                dot += f'\t{vidx} -> {uidx} [{info}]\n'

    dot += "}\n"
    return dot


def unmat_to_dot(G,
                 vex_info=partial(identity, ""),
                 edge_exists=lambda e: e is not None,
                 edge_info=partial(identity, "")):

    dot = "graph {\n"
    for vidx in range(len(G)):
        info = _format(vex_info(vidx), ",")
        dot += f'\t{vidx} [{info}]\n'
        for uidx in range(vidx):
            e = G[vidx][uidx]
            if edge_exists(e):
                info = _format(edge_info(vidx, uidx, e), ",")
                dot += f'\t{vidx} -- {uidx} [{info}]\n'

    dot += "}\n"
    return dot


def mat_to_adj(mat, is_edge=lambda e: e is not None):
    G = []
    for vidx in range(len(mat)):
        adj = []
        for uidx in range(len(mat)):
            if is_edge(mat[vidx][uidx]):
                adj.append(uidx)
        G.append(adj)

    return G


if __name__ == "__main__":
    from pprint import pprint
    pprint(mat_to_adj([
        [0, 20, 10, 3, 0, 0],
        [20, 0, 0, 16, 0, 0],
        [10, 0, 0, 17, 15, 0],
        [3, 16, 17, 0, 20, 18],
        [0, 0, 15, 20, 0, 14],
        [0, 0, 0, 18, 14, 0],
    ], is_edge=lambda e: e != 0))
