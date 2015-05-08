import sys
import os
import itertools
from Graph import *
import pdb
from scorer_single import *
from solver import *
from validator import *

graph = generate_graph('8x8.in', 'input_files/8x8.in')
def brute_force(graph):
    #pdb.set_trace()
    gen = itertools.permutations(range(1, graph.quantity_nodes+1))
    #pdb.set_trace()
    item = list(gen)
    best_path = []
    best_cost = graph.cost_path(item[0])
    #print item
    for i in item:
        #print ("i: ", i )
        #print ("graph.cost_path(i)", graph.cost_path(i), "\n")
        if graph.cost_path(i) < best_cost and graph.valid_path(i):
            best_cost = graph.cost_path(i)
            best_path = i
    #print item
    print "best path: ", best_path
    print "path cost: ", best_cost
    #pdb.set_trace()
    return best_path

brute_force(graph)
