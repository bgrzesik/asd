# https://faliszew.github.io/algograf/lab2
# Bartłomiej Grzesik (jest dwóch Bartłomieji :) )

from dimacs import loadDirectedWeightedGraph, readSolution
from sys import argv
import math

# (V,L) = loadDirectedWeightedGraph(argv[1])
TEST = "graphs/connectivity/clique100"
(V,L) = loadDirectedWeightedGraph(TEST)

A = [ [] for i in range(V + 1) ] # off 1
A[0] = None

W = {}
F = {}

for (x, y, c) in L:
    W[(x, y)] = c

    A[x].append(y)
    A[y].append(x)

    F[(x, y)] = 0
    F[(y, x)] = 0

""""
def find_path():
    global A, W, F
    parent = [None] * len(A)
    the_max = 0

    def visit(u, max_flow):
        global A, W, F
        nonlocal parent, the_max

        if parent[-1] is not None:
            if u == len(parent) - 1:
                the_max = max_flow
            return

        for v in A[u]:
            if v == 1:
                continue;

            cap = None

            if (u, v) in W:
                cap = W[(u, v)] - F[(u, v)]
            elif (v, u) in W:
                cap = F[(v, u)]
            else:
                assert False

            if cap == 0:
                continue;

            if parent[v] is None:
                parent[v] = u
                visit(v, min(cap, max_flow))

    visit(1, math.inf)
    return parent, the_max
"""


def find_path():
    global A, W, F

    parent = [None] * len(A)
    queue = [(1, math.inf)]

    while queue:
        u, max_cap = queue.pop(0)

        if u == len(A) - 1:
            return parent, max_cap

        for v in A[u]:
            if v == 1:
                continue;

            if (u, v) in W:
                cap = W[(u, v)] - F[(u, v)]
            elif (v, u) in W:
                cap = F[(v, u)]
            else:
                assert False

            if cap == 0:
                continue

            if parent[v] is None:
                parent[v] = u

                queue.append((v, min(max_cap, cap)))

    return parent, 0

parent, the_max = find_path()
while parent[-1] is not None:
    # print(parent, the_max)

    v = len(A) - 1
    while parent[v] is not None:
        # print(parent[v])
        if (parent[v], v) in W:
            F[(parent[v], v)] += the_max
        else:
            F[(v, parent[v])] -= the_max

        v = parent[v]


    parent, the_max = find_path()

result = sum([ F[(1, v)] for v in A[1] ])
correct = int(readSolution(TEST))
print(result, correct, result == correct)










