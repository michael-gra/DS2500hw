'''
    Grace Michael
    DS2500
    Spring 2021
    Graph/inheritance lab - weighted graph child class starter code
'''

from graph import Graph

class WeightedGraph(Graph):
    ''' This class WeightedGraph inherits from Graph
        So it'll start off with all the same attributes and methods
        TODO:
            - Finish writing the add_edge method so that it udpates
              edge_wt.
            - Write a get_path_weight method that sums together all
              the weights along a path, where a path is a list of vertices
    '''
    def __init__(self):
        super().__init__()
        self.edge_wt = {}

    def add_edge(self, node, neighbor, weight):
        super().add_edge(node, neighbor)
        self.edge_wt[(node, neighbor)] = weight

    def get_path_weight(self, path):
        weight = 0
        for v in range(len(path) -1):
            weight += self.edge_wt[(path[v], path[v +1])]
        return weight



'''
(WVH, ISEC)
(WVH, WVF)
(WVH, Shillman)
(WVF, ISEC)
(ISEC, Dodge)
(ISEC, WVF)
(ISEC, WVH)
(Shillman, Dunkin)
(Dunkin, ISEC)
(Dunkin, Shillman)

['WVH', 'ISEC', 'Dodge']
['WVH', 'Shillman', 'Dunkin']
['ISEC', 'Dodge']
['Shillman', 'Dunkin', 'ISEC', 'Dodge']
['WVH', 'Shillman', 'Dunkin']
['WVH', 'ISEC']
(WVH, ISEC)
(WVH, WVF)
(WVH, Shillman)
(WVF, ISEC)
(ISEC, Dodge)
(ISEC, WVF)
(ISEC, WVH)
(Shillman, Dunkin)
(Dunkin, ISEC)
(Dunkin, Shillman)

4 : ['WVH', 'ISEC', 'Dodge']
4 : ['WVH', 'Shillman', 'Dunkin']
1 : ['ISEC', 'Dodge']
7 : ['Shillman', 'Dunkin', 'ISEC', 'Dodge']
4 : ['WVH', 'Shillman', 'Dunkin']
3 : ['WVH', 'ISEC']
'''
