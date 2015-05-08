class Graph_kyle(object):

    def __init__(self, matrix_graph, order_colors = None):
        self.matrix_graph = matrix_graph
        self.quantity_nodes = len(matrix_graph)
        self.color_of_nodes = {}
        self.colors = order_colors

        for x in range(self.quantity_nodes):
            if 'R' == order_colors[x]:
                self.color_of_nodes[x + 1] = 'red'
            else:
                self.color_of_nodes[x + 1] = 'blue'

    def assign_colors(self, index_node, c):
        self.color_of_nodes[index_node] = c


    def find_neighbors(self, node):
        neighbors = {}
        for x in range(1, self.quantity_nodes + 1):
            if node != x:
                neighbors[x] = self.cost_edge(node, x)
        return neighbors


    def color_node(self, index_node):
        return self.color_of_nodes[index_node]


    def cost_edge(self, endpoint1, endpoint2):
        edge_cost = self.matrix_graph[endpoint1 - 1][endpoint2 - 1]
        return edge_cost


    def cost_path(self, p):
        path_cost = 0
        for node in range(1, len(p)):
            path_cost += self.cost_edge(p[node - 1], p[node])
        return path_cost


    def amount_nodes(self):
        return self.quantity_nodes


    def oppo_color(self, c):
        if 'red' == c:
            return 'blue'
        else:
            return 'red'
