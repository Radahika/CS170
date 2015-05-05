from Graph import Graph
import sys

def path_finder(g):
    """return NPTSP path with lowest cost"""
    return

def legitimate_path(g, p):
    """checks validity of path"""
    return

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
    title = 'input_files/{0}.in'.format(index_file)
    with open(title) as data:
        nodes = int(data.readline())
        matrix_graph = [[] for i in range(nodes)]
        for i in range(nodes):
            matrix_graph[i] = [int(k) for k in data.readline().split()]
        order_colors = data.readline()
    g = Graph(matrix_graph, order_colors)
    return path_finder(g)

# if __name__ == '__main__':
#     output(int(sys.argv[1]))