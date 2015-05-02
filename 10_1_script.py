i = 0
j = 0
N = 50
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
        if matrix[j][i] == 0:
            matrix[i][j] = random.randrange(6, 60)
        else:
            matrix[i][j] = matrix[j][i]

        if i == j:
            matrix[i][j] = 0
        if i == j+1 and matrix[j+1][i] == 0:
             rand_num = random.randrange(12, 17)
             matrix[i][j] = rand_num
             matrix[j][i] = matrix[i][j]
        elif i == j+1:
             matrix[i][j] = matrix[j+1][i]


edges =  matrix[N-1]
for i in range(1, N-1):
    rand_num = random.randrange(70, 100)
    edges[i] = rand_num
    matrix[i][N-1] = rand_num

pretty_print(matrix)
