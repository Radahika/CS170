import sys
import os
import itertools
from Graph import *
import pdb
from scorer_single import *
from solver import *

graph = generate_graph('8x8.in', 'input_files/8x8.in')
def brute_force(graph):
    pdb.set_trace()
    gen = itertools.permutations(range(1, graph.quantity_nodes+1))
    pdb.set_trace()
    item = list(gen)
    best_path = []
    best_cost = graph.cost_path(item[0])
    for i in item:
        if graph.cost_path(i) < best_cost:
            best_path = i
    #print item
    print best_path
