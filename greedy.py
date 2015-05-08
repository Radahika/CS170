import linecache #lines are 1 indexed
import sys
import random
import re


#only call this on lines in the matrix. will err otherwise.
def convert(file_name, node_index):
	line = linecache.getline(file_name, node_index+1)
	line = line[2:line.index('\n')]
	line = line.split()
	line = [int(i) for i in line]
	return line



#current issue: if more than one node with same cost, only chooses first one
def cheapest(file_name, node, repeat, visited):
	n = 1

	# print local_current
	for_index = convert(file_name, node)
	local_current = convert(file_name, node)
	possibilities = []
	colors = linecache.getline(file_name, len(for_index)+2)

	color = for_index[node-1]

	if repeat == 3:
		for i in len(for_index):
			if (color != colors[i]) and (i+1 not in visited) and (i != node-1):
				possibilities.append(for_index[i])
	if possibilities == []:
		n = random.choice(possibilities)
		return [for_index[n], n]
	return [min(possibilities), for_index.index(min(possibilities))]


	# while n < order:
	# 	if local_current == []:
	# 		if for_index.index(max(for_index)) in visited:
	# 			n = random.choice(visited)
	# 			return [for_index[n], n]
	# 		return [max(for_index), for_index.index(max(for_index))]
	# 	local_current.remove(min(local_current))
	# 	# print n, "\n", order
	# 	n+=1
	# 	if n == order and (for_index.index(min(local_current)) in visited):
	# 		n-=1
	# if min(local_current) == 0:
	# 	indices = [i for i, x in enumerate(for_index) if x == 0]
	# 	indices.remove(node-1)
	# return [min(local_current), for_index.index(min(local_current))]


def greedy(file_name, N):
	# size = int(x) for x in f.readline().split() #read first line - size
	# starting_nodes = range(1, size+1) #list (0, ..., size-1)
	"""cheapest(file_name, node, order)
	returns the cost and index of where to travel next """
	curr_node = random.randrange(1, N+1) #initialize next as random variable
	return_path = []
	color_list = linecache.getline(file_name, N+2)
	repeat_colors = 1 #can't be greater than 3
	curr_color = color_list[curr_node]
	visited = []

	while len(visited) < N:
		index_list = convert(file_name, curr_node) #outgoing edge weights for current node
		if cheapest(file_name, curr_node, 1, visited):
			(choice_cost, choice) = cheapest(file_name, curr_node, 1, visited)
			visited.append(choice)
		else:
			#restart
			return_path = []
			curr_node = random.randrange(1, N+1)
			repeat_colors = 1
			curr_color = color_list[curr_node]
			continue
		choice_color = color_list[choice-1]

		#LOOP - if next move is an illegal color, get second cheapest
		if repeat_colors == 3:
			i = 2
			while choice_color == curr_color:
				(choice_cost, choice) = cheapest(file_name, curr_node, i, visited)
				visited.append(choice)
				choice_color = color_list[choice - 1]
				i += 1
		if choice_color == curr_color:
			repeat_colors += 1
		else:
			repeat_colors = 0
		return_path.append(choice)
		visited.append(choice)
		curr_node = choice
		curr_color = color_list[choice-1]
	return return_path



# T = 1 # number of test cases
# fout = open ("answer.out", "w")
# for t in xrange(1, T+1):
#     fin = open(str(t) + ".in", "r")
#     N = int(fin.readline()) #size
#     d = [[] for i in range(N)] #turn each row into array of integers
#     for i in xrange(N):
#         d[i] = [int(x) for x in fin.readline().split()]
#     c = fin.readline() #print out row 

#     # find an answer, and put into assign
#     # assign = [0] * N
#     assign = greedy(fin, str(t) + ".in", N) #call greedy strategy
#     for i in xrange(N):
#         assign[i] = i+1

#     fout.write("%s\n" % " ".join(map(str, assign)))
# fout.close()



