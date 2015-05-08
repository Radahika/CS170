import os
import pdb
from solver import *

RC = []
for filename in os.listdir('instances'):
    path = os.path.join('instances', filename)
    g = generate_graph(filename, path)
    #pdb.set_trace()
    if hard_code(g):
        RC.append((filename, hard_code(g)))

print RC
