'''
    DS2500
    Spring 2021
    Code from lecture -- a Graph class

    G = (V, E) vertices and edges

    We describe an edge in terms of its vertices
    edge (u, v) is an edge from vertex u to vertex v
    u --> v

    v is one of u's neighbors, but not vice-versa
'''

import collections as col

class Graph:

    def __init__(self):
        self.G = {}

    def add_vertex(self, v):
        if v not in self.G:
            self.G[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.G[u].add(v)

    def __str__(self):
        s = ""
        for vertex in self.G:
            s += vertex + " ["
            for neighbor in self.G[vertex]:
                s += neighbor + ", "
            s += "]\n"
        return s


    def shortest_path(self, start, end):
        backtrack = {} # When visiting a node, remember where you came from
        visited = {start} # The set of nodes that have been visited already
        Q = col.deque()
        Q.appendleft(start)

        # Visit all nodes using bfs and save backtrack info
        while len(Q) > 0: # Q is not empty
            current = Q.pop()
            adj = self.G[current]
            for v in adj:
                if v not in visited:
                    visited.add(v)
                    Q.appendleft(v)
                    backtrack[v] = current

        # Construct path from start to end by working backward from the end
        path = []
        current = end
        while current != start:
            path.append(current)
            if current not in backtrack: # No path start->end exists
                return []
            current = backtrack[current]

        # Complete the path
        path.append(start)
        path.reverse()
        return path
