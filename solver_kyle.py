from Graph_kyle import Graph_kyle
import sys
from itertools import *

PERMUTE_CAP = 10
GRAPHS_COUNT = 3

def path_finder(g):
    """return NPTSP path with lowest cost"""
    if g.amount_nodes() <= PERMUTE_CAP:
        return brute_force(g)
    else:
        return greedy_algorithm(g)


def legitimate_path(g, p):
    """checks validity of path"""
    present_color = None
    count = 0
    for i in range(len(p)):
        node_color = g.color_node(p[i])
        if node_color == present_color:
            count += 1
        else:
            present_color = node_color
            count = 1
        if 3 < count:
            return False
    return True


def brute_force(g):
    """go through all permutations of possible paths if graph is small enough"""
    nodes = []
    for n in range(1, g.amount_nodes() + 1):
        nodes.append(n)
    optimal_path = None
    optimal_cost = sys.float_info.max
    for p in permutations(nodes):
        if legitimate_path(g, p):
            path_cost = g.cost_path(p)
            if optimal_cost > path_cost:
                optimal_path = p
                optimal_cost = path_cost
    optimal_path = list(optimal_path)
    return optimal_path


def greedy_algorithm(g):
    return


def greedy_helper(g, s_node):
    return


def cheapest_neighbor(neighbors):
    """takes in a dictionary where keys = nodes and their values = costs"""
    min_cost = min(neighbors.values())
    for node in neighbors:
        if min_cost == neighbors[node]:
            return node


def output():
    solutions = []
    for x in range(GRAPHS_COUNT):
        index_file = 'instances/{0}.in'.format(x + 1)
        solutions.append(read_input(index_file))
    with open('answer.out', 'w') as output:
        for s in solutions:
            output.write(' '.join(map(str, s)) + '\n')


def read_input(index_file):
    with open(index_file) as data:
        nodes = int(data.readline())
        matrix_graph = []
        for i in range(nodes):
            matrix_graph.append([])
        for i in range(nodes):
            for x in data.readline().split():
                matrix_graph[i].append(int(x))
        order_colors = data.readline()
    g = Graph(matrix_graph, order_colors)
    return path_finder(g)


if __name__ == '__main__':
    output()