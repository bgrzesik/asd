import math
from queue import Queue
from pprint import pprint
from dimacs import loadDirectedWeightedGraph, readSolution
from dataclasses import dataclass, field


@dataclass
class Edge(object):
    tail: int
    head: int
    capacity: int
    flow: int = 0


@dataclass
class Vertex(object):
    index: int 
    excess: int = 0
    height: int = 0
    current: int = 0
    adj: list = field(default_factory=list, repr=False)


@dataclass
class Graph(object):
    solution: int
    vertices: list
    edges: list = field(default_factory=list)
    queue: list = field(default_factory=Queue)


def load_graph(f: str) -> Graph:
    V, E = loadDirectedWeightedGraph(f)

    graph = Graph(solution=int(readSolution(f)), 
                  vertices=[Vertex(v) for v in range(V + 1)])

    graph.vertices[0] = None
    for tail, head, cap in E:
        edge = Edge(tail, head, cap)
        graph.edges.append(edge) 
        graph.vertices[head].adj.append(edge)
        graph.vertices[tail].adj.append(edge)

    return graph



def push(graph: Graph, edge: Edge, tail_idx: int):

    tail = graph.vertices[edge.tail]
    head = graph.vertices[edge.head]

    excess = tail.excess if tail_idx == edge.tail else head.excess

    if edge.tail == tail_idx:
        # regular
        flow = min(excess, edge.capacity - edge.flow)
        edge.flow += flow

        tail.excess -= flow
        head.excess += flow
    else:
        # residual
        flow = min(excess, edge.flow)
        edge.flow -= flow

        tail.excess += flow
        head.excess -= flow

def relabel(vertex: Vertex):
    m = math.inf

    for edge in vertex.adj:
        if edge.tail == vertex.index:
            neighbor = graph.vertices[edge.head]
            avail = edge.capacity - edge.flow
        else:
            neighbor = graph.vertices[edge.tail]
            avail = edge.flow

        if avail > 0:
            m = min(m, neighbor.height)

    vertex.height = 1 + m

def discharge(graph: Graph, vertex: Vertex):
    while vertex.excess > 0:
        if vertex.current >= len(vertex.adj):
            relabel(vertex)
            vertex.current = 0
            continue
            
        edge = vertex.adj[vertex.current]

        if edge.tail == vertex.index:
            neighbor = graph.vertices[edge.head]
            avail = edge.capacity - edge.flow
        else:
            neighbor = graph.vertices[edge.tail]
            avail = edge.flow

        if avail > 0 and vertex.height == neighbor.height + 1:
            push(graph, edge, vertex.index)
        else:
            vertex.current += 1


def maxflow(graph: Graph):
    source = 1
    target = len(graph.vertices) - 1

    for vertex in graph.vertices[1:]:
        vertex.height = 0
        vertex.excess = 0

    for edge in graph.edges:
        edge.flow = 0

    source_vertex = graph.vertices[source]
    source_vertex.height = len(graph.vertices) - 1

    for edge in source_vertex.adj:
        if edge.tail != source:
            continue

        edge.flow = edge.capacity
        graph.vertices[edge.head].excess = edge.capacity
        source_vertex.excess -= edge.capacity

    index = 2
    
    while index < len(graph.vertices) - 1:
        vertex = graph.vertices[index]
        old_height = vertex.height

        discharge(graph, vertex)

        if vertex.height > old_height:
            index = 2
        else:
            index += 1

    return sum([edge.flow for edge in graph.vertices[target].adj])
        
        

if __name__ == "__main__":
    graph = load_graph("graphs/flow/simple")
    result = maxflow(graph)
    print(result, graph.solution)

    graph = load_graph("graphs/flow/simple2")
    result = maxflow(graph)
    print(result, graph.solution)

    graph = load_graph("graphs/flow/grid5x5")
    result = maxflow(graph)
    print(result, graph.solution)








