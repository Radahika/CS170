i = 0
j = 0
N = 50
W = 20
matrix = [[0 for x in range(N)] for x in range(N)]
import random

def pretty_print(A):
    print N
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in A]))
    print "AB"*N
    print ""

for i in range(N):
    for j in range(N):
        if i == j:
            matrix[i][j] = 0
        elif matrix[j][i] == 0:
            matrix[i][j] = random.randrange(5, 60)
        else:
            matrix[i][j] = matrix[j][i]

edges =  matrix[N-1]
for i in range(1, N-1):
    edges[i] += W
    matrix[i][N-1] += W


pretty_print(matrix)
