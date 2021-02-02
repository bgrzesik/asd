import networkx as nx
import networkx.algorithms.planarity as nx_planartiy
import networkx.algorithms.flow as nx_flow
import networkx.algorithms.components as nx_components
import networkx.algorithms.dag as nx_dag

from dimacs import loadWeightedGraph, readSolution, loadCNFFormula


# import check_planarity

def load_graph(name):
    G = nx.Graph()

    (V, L) = loadWeightedGraph(name)
    G.add_nodes_from(range(1, V + 1))
    G.add_edges_from([(u, v) for u, v, _ in L])

    return V, G

def load_digraph(name):
    G = nx.DiGraph()

    (V, L) = loadWeightedGraph(name)
    G.add_nodes_from(range(1, V + 1))

    for u, v, cost in L:
        G.add_edge(u, v)
        G[u][v]["capacity"] = cost

    return V, G


if __name__ == "__main__":
    TESTS = [
        "graphs-lab6/plnar/AT",
        "graphs-lab6/plnar/16-cell",
        "graphs-lab6/plnar/cycle",
        "graphs-lab6/plnar/clique5",
        "graphs-lab6/plnar/K33",
        "graphs-lab6/plnar/petersen",
    ]

    for name in TESTS:
        print(name)
        _, G = load_graph(name)

        is_planar = readSolution(name) == "1"
        nx_planar = nx_planartiy.check_planarity(G)[0]

        if nx_planar ^ is_planar:
            print("NX FAILED :O")




if __name__ == "__main__":
    TESTS = [
        "graphs-lab2/flow/clique20",
        "graphs-lab2/flow/pp100",
        "graphs-lab2/flow/simple2",
        "graphs-lab2/flow/trivial2",
        "graphs-lab2/flow/trivial",
    ]

    for name in TESTS:
        print(name)
        V, G = load_digraph(name)
        correct = int(readSolution(name))
        flow = nx_flow.maximum_flow(G, 1, V)[0]

        if correct != flow:
            print("NX Failed :O") 















def cnf2_sat(name):
    V, F = loadCNFFormula(name)

    G = nx.DiGraph()

    for x, y in F:
        G.add_edge(-x, y)
        G.add_edge(-y, x)

    sccs = nx_components.strongly_connected_components(G)
    sccs = list(sccs)

    for i, scc in enumerate(sccs):
        for v in scc:
            G.nodes[v]["scc"] = i

            if "scc" in G.nodes[-v] and G.nodes[-v]["scc"] == G.nodes[v]["scc"]:
                return False, None

    H = nx.DiGraph()

    for u, v in G.edges:
        u_scc = G.nodes[u]["scc"]
        v_scc = G.nodes[v]["scc"]

        if u_scc == v_scc:
            continue

        if not H.has_edge(u_scc, v_scc):
            H.add_edge(u_scc, v_scc)

    # print(H)
    topo = nx_dag.topological_sort(H)
    # topo = list(topo)

    values = {}

    for i in topo:
        scc = sccs[i]

        for v in scc:
            vi = abs(v)
            if vi not in values:
                values[vi] = v < 0
            # if v < 0 and -v not in values: # not V
            #     values[-v] = True
            # elif v > 0 and v not in values:
            #     values[v] = False

    # print(F)
    # print(values)

    if False:
        for x, y in F:
            xx = (x > 0) ^ (not values[abs(x)])
            yy = (y > 0) ^ (not values[abs(y)])

            # print(xx, yy)
            # print(x, y)

            if not (xx or yy):
                assert False


    return True, values



if __name__ == "__main__":
    TESTS = [
        "sat/simple_sat",
        "sat/simple_unsat",
        "sat/sat5_10",
        "sat/sat5_20",
        "sat/sat15_30",
    ]

    for name in TESTS:
        print(name)
        sat, values = cnf2_sat(name)
        correct = readSolution(name)[-1] == "1"

        if sat ^ correct:
            print(f"FAILED {name}")







