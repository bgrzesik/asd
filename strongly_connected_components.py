from graph_util import mat_to_dot


class Vertex:
    def __init__(self):
        # self.adj = adj
        self.visited = False
        self.process_time = None
        self.component = None


def strongly_connected_components(G):
    time = 0
    component = 0

    n = len(G)

    verticies = [Vertex() for _ in range(n)]

    def time_vertex(vidx):
        nonlocal G, time

        v = verticies[vidx]
        v.visited = True

        for uidx in range(n):
            if G[vidx][uidx] is None:
                continue

            u = verticies[uidx]
            if not u.visited:
                time_vertex(uidx)

        v.process_time = time
        time += 1

    def mark_component(vidx):
        nonlocal G, component

        v = verticies[vidx]
        v.visited = True

        for uidx in range(n):
            if G[uidx][vidx] is None:
                continue

            u = verticies[uidx]
            if not u.visited:
                mark_component(uidx)

        v.component = component

    for i in range(n):
        if not verticies[i].visited:
            time_vertex(i)

    order = list(range(n))
    order.sort(key=lambda e: verticies[e].process_time, reverse=True)

    for v in verticies:
        v.visited = False

    for vidx in order:
        if not verticies[vidx].visited:
            mark_component(vidx)
            component += 1

    return verticies


if __name__ == "__main__":
    G = [
        [None, 1, None, None, None, None, None, None, None, 1, None],
        [None, None, 1, None, None, None, None, None, None, None, None],
        [1, None, None, None, 1, None, None, None, None, None, None],
        [None, None, None, None, None, 1, None, None, None, None, None],
        [None, None, None, 1, None, None, 1, None, None, None, None],
        [None, None, None, None, 1, None, None, None, None, None, None],
        [None, None, None, None, None, 1, None, None, None, None, None],
        [None, None, None, None, None, None, 1, None, None, 1, None],
        [None, None, None, None, None, None, None, 1, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, 1],
        [None, None, None, None, None, 1, None, None, 1, None, None],
    ]

    vert = strongly_connected_components(G)
    print(mat_to_dot(
        G, vex_info=lambda v: f'label="{v}\\ncomponent={vert[v].component}\\nprocess_time={vert[v].process_time}"'))
