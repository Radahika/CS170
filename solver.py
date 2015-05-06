from Graph import Graph
import sys
import pdb
from validator import *

def path_finder(g):
    """return NPTSP path with lowest cost"""
    print g
    return

def hard_code(g):
    if g == r1:
        return "1"
    elif g == r2:
        return "2"
    elif g == r3:
        return "3"

def legitimate_path(g):
    """checks validity of path"""
    return processFile(g.s)

def brute_force(g):
    """go through all permutations of possible paths if graph is small enough"""
    return

def output(input_quantity):
    solutions = []
    for x in range(1, input_quantity + 1):
        solutions.append(read_input(x))
    with open('answer.txt', 'w') as answer:
        for p in solutions:
            answer.write('%s\n'%' '.join(map(str, p)))

def read_input(index_file):
    g = generate_graph(index_file)
    return path_finder(g)

# if __name__ == '__main__':
#     output(int(sys.argv[1]))

def generate_graph(index_file):
    filename = '{0}.in'.format(index_file)
    pathname = 'input_files/{0}.in'.format(index_file)
    with open(pathname) as data:
        nodes = int(data.readline())
        matrix_graph = [[] for i in range(nodes)]
        for i in range(nodes):
            matrix_graph[i] = [int(k) for k in data.readline().split()]
        order_colors = data.readline()
    g = Graph(matrix_graph, filename, pathname, order_colors)
    return g


r1 = generate_graph('RackCity1')
r2 = generate_graph('RackCity2')
r3 = generate_graph('RackCity3')
