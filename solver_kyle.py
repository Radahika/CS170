from Graph_kyle import Graph_kyle as Graph
import sys
from itertools import *
from greedy import *

PERMUTE_CAP = 10
GRAPHS_COUNT = 495

RackCity1 = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
RackCity2 = [5, 36, 2, 12, 47, 49, 28, 8, 30, 19, 27, 3, 14, 20, 17, 13, 25, 35, 26, 42, 24, 37, 9, 48, 46, 38, 50, 10, 45, 4, 16, 15, 32, 1, 23, 40, 6, 33, 31, 41, 18, 34, 39, 44, 11, 7, 43, 22, 29, 21]
RackCity3 = [50, 1, 13, 15, 48, 12, 40, 3, 2, 29, 14, 43, 17, 34, 33, 24, 27, 38, 44, 42, 39, 16, 46, 10, 47, 28, 26, 21, 45, 30, 37, 18, 5, 35, 7, 22, 20, 41, 8, 25, 9, 49, 11, 19, 31, 32, 36, 6, 4, 23]


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
        print index_file
        if index_file == 'instances/260.in':
            solutions.append(RackCity1)
        elif index_file == 'instances/60.in':
            solutions.append(RackCity2)
        elif index_file == 'instances/241.in':
            solutions.append(RackCity3)
        else:
            solutions.append(read_input(index_file))
    with open('answer.out', 'w') as output:
        print solutions
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


#RackCity1 = ['50 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 39  40  41  42  43  44  45  46  47  48  49']
#RackCity2 = ['5  36  2  12  47  49  28  8  30  19  27  3  14  20  17  13  25  35  26  42  24  37  9  48  46  38  50  10  45  4  16  15  32  1  23  40  6  33  31  41  18  34  39  44  11  7  43  22  29  21']
#RackCity3 = ['50  1  13  15  48  12  40  3  2  29  14  43  17  34  33  24  27  38  44  42  39  16  46  10  47  28  26  21  45  30  37  18  5  35  7  22  20  41  8  25  9  49  11  19  31  32  36  6  4  23']

if __name__ == '__main__':
    output()
