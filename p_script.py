i = 0
j = 0
N = 5
W = 20
matrix = [[0 for x in range(N)] for x in range(N)]
import random
import pdb

def pretty_print(A):
    print N
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in A]))
    print "RB"*(N/2)
    print ""

for i in range(N):
    for j in range(N):
        if i == j:
            matrix[i][j] = 0
        elif matrix[j][i] == 0:
            matrix[i][j] = random.randrange(6, 60)
        else:
            matrix[i][j] = matrix[j][i]


pretty_print(matrix)
