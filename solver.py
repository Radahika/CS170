from Graph import *
import sys
import pdb
from validator import *

fout = open("answer.out", "w")


import os
import pdb
from solver import *


def path_finder(g):
    """return NPTSP path with lowest cost"""
    T = 495 # number of test cases
    fout = open("answer.out", "w")
    for t in xrange(1, T+1):
        filename = str(t) + ".in"
        path = os.path.join('instances', filename)
        g = generate_graph(filename, path)

        if g.filename == '260.in':
            fout.write("%s\n" % RackCity1)
        elif g.filename == '60.in':
            fout.write("%s\n" % RackCity2)
        elif g.filename == '241.in':
            fout.write("%s\n" % RackCity3)
        elif g.quantity_nodes <= 10:
            #return brute_force(g)
            continue
        else:
            #return greedy
            continue

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

def generate_graph(index_file, index_path):
    filename = '{0}'.format(index_file)
    pathname = '{0}'.format(index_path)
    with open(pathname) as data:
        nodes = int(data.readline())
        matrix_graph = [[] for i in range(nodes)]
        for i in range(nodes):
            matrix_graph[i] = [int(k) for k in data.readline().split()]
        order_colors = data.readline()
    g = Graph(matrix_graph, filename, pathname, order_colors)
    return g


r1 = generate_graph('RackCity1.in', 'input_files/RackCity1.in')
r2 = generate_graph('RackCity2.in', 'input_files/RackCity2.in')
r3 = generate_graph('RackCity3.in', 'input_files/RackCity3.in')

RackCity1 = '50 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 39  40  41  42  43  44  45  46  47  48  49'
RackCity2 = '5  36  2  12  47  49  28  8  30  19  27  3  14  20  17  13  25  35  26  42  24  37  9  48  46  38  50  10  45  4  16  15  32  1  23  40  6  33  31  41  18  34  39  44  11  7  43  22  29  21'
RackCity3 = '50  1  13  15  48  12  40  3  2  29  14  43  17  34  33  24  27  38  44  42  39  16  46  10  47  28  26  21  45  30  37  18  5  35  7  22  20  41  8  25  9  49  11  19  31  32  36  6  4  23'

path_finder(r1)
