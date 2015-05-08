import pdb
from scorer_single import *

class Graph(object):

    def __init__(self, matrix_graph, filename, pathname, order_colors = None):
        self.matrix_graph = matrix_graph
        self.quantity_nodes = len(matrix_graph)
        self.color_of_nodes = {}
        self.filename = filename
        self.pathname = pathname

        if order_colors:
            for x in range(len(order_colors)):
                if order_colors[x] == 'B':
                    self.color_of_nodes[x+1] = 'blue'
                else:
                    self.color_of_nodes[x+1] = 'red'
        else:
            for node in range(1, self.quantity_nodes+1):
                self.color_of_nodes[node] = None


    def assign_colors(self, index_node, c):
        self.color_of_nodes[index_node] = c


    def find_neighbors(self, node):
        neighbors = {}
        for x in range(1, self.quantity_nodes+1):
            if x != node:
                neighbors[x] = self.cost_edge(node, x)
        return neighbors

    def color_of_vertex(self, index_node):
        return self.color_of_nodes[index_node]

    def cost_edge(self, endpoint1, endpoint2):
        return self.matrix_graph[endpoint1-1][endpoint2-1]

    def cost_path(self, path):
        #make sure the path is a file with the path listed to use processCase
        assert(os.path.isfile(path))
        return processCase(self.filename, path)

    def quantity_nodes(self):
        return self.quantity_nodes

    def __repr__(self):
        with open(self.pathname, 'r') as fin:
            return fin.read()

    def __eq__(self, other):
        return self.color_of_nodes == other.color_of_nodes and self.matrix_graph == other.matrix_graph
