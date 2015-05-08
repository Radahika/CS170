import sys
import os
import itertools
from Graph import *
import pdb
from scorer_single import *
from solver import *

graph = generate_graph('RackCity1.in', 'input_files/RackCity1.in') 
def brute_force(graph): 
    gen = itertools.permutations(range(1, graph.quantity_nodes))
    print gen 
