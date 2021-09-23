'''
    DS2500
    Spring 2021
    Sample code from class -- Graphs and Networks representing the
    NEU Boston campus.

    Vertices are buildings on capus
    Weights on edges are how long it takes to walk from one vertex to another
'''

from graph import Graph
from weighted_graph import WeightedGraph

if __name__ == "__main__":
    g = Graph()
    g.add_edge("WVH", "WVF")
    g.add_edge("WVF", "ISEC")
    g.add_edge("ISEC", "Dodge")
    g.add_edge("WVH", "Shillman")
    g.add_edge("Dunkin", "ISEC")
    g.add_edge("ISEC", "WVF")
    g.add_edge("Shillman", "Dunkin")
    g.add_edge("Dunkin", "Shillman")
    g.add_edge("WVH", "ISEC")
    g.add_edge("ISEC", "WVH")

    print(g)

    path = g.shortest_path("WVH", "Dodge")
    print(path)

    path = g.shortest_path("WVH", "Dunkin")
    print(path)

    path = g.shortest_path("ISEC", "Dodge")
    print(path)

    path = g.shortest_path("Shillman", "Dodge")
    print(path)

    path = g.shortest_path("WVH", "Dunkin")
    print(path)

    path = g.shortest_path("WVH", "ISEC")
    print(path)

    wg = WeightedGraph()
    wg.add_edge("WVH", "WVF", 2)
    wg.add_edge("WVF", "ISEC", 3)
    wg.add_edge("ISEC", "Dodge", 1)
    wg.add_edge("WVH", "Shillman", 2)
    wg.add_edge("Dunkin", "ISEC", 4)
    wg.add_edge("ISEC", "WVF", 3)
    wg.add_edge("Shillman", "Dunkin", 2)
    wg.add_edge("Dunkin", "Shillman", 2)
    wg.add_edge("WVH", "ISEC", 3)
    wg.add_edge("ISEC", "WVH", 3)

    print(wg)
    path = wg.shortest_path("WVH", "Dodge")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)

    path = wg.shortest_path("WVH", "Dunkin")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)

    path = wg.shortest_path("ISEC", "Dodge")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)

    path = wg.shortest_path("Shillman", "Dodge")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)

    path = wg.shortest_path("WVH", "Dunkin")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)

    path = wg.shortest_path("WVH", "ISEC")
    wt = wg.get_path_weight(path)
    print(wt, ":", path)
