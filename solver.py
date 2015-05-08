from Graph import Graph
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
    same_color_count = 0
    for i in range(len(p)):
        node_color = g.color_node(p[i])
        if node_color == present_color:
            same_color_count += 1
        else:
            present_color = node_color
            same_color_count = 1
        if 3 < same_color_count:
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
    optimal_path = None
    optimal_cost = sys.float_info.max
    for s_node in range(1, g.amount_nodes() + 1):
        p, path_cost = greedy_helper(g, s_node)
        if path_cost < optimal_cost:
            optimal_cost = path_cost
            optimal_path = p
    print "length", len(optimal_path)
    print "path", optimal_path
    return optimal_path  


def greedy_helper(g, s_node):
    p = [s_node]
    current_node = s_node
    current_color = g.color_node(s_node) 
    count = 1
    while len(p) < g.amount_nodes():
        neighbors = g.find_neighbors(current_node)
        for node in neighbors.keys():
            # print "node",node
            # print "path", p
            if node in p:
                # print "hello"
                del neighbors[node]
                continue
            if g.color_node(node) == current_color:
                if count == 3:
                    del neighbors[node]
        # print neighbors
        if cheapest_neighbor(neighbors) != None:
            next = cheapest_neighbor(neighbors)
        # print "next:", next
        if next != None:
            if g.color_node(next) == current_color:
                count += 1
            else:
                current_color = g.oppo_color(g.color_node(next))
                count = 1
        if next not in p:
            p.append(next)
            current_node = next
            current_color = g.color_node(current_node)
        # print "current node",current_node
    return (p, g.cost_path(p)) #return a path and its cost



    # neighbors = g.find_neighbors(p[-1])




def cheapest_neighbor(neighbors):
    """takes in a dictionary where keys = nodes and their values = costs"""
    # min_cost = min(neighbors.values())
    # # print min_cost

    # for node in neighbors:
    #     if min_cost == neighbors[node]:
    #         return node
    min_cost = sys.float_info.max
    next = None
    for node in neighbors:
        if neighbors[node] < min_cost:
            min_cost = neighbors[node]
            next = node
    return next


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