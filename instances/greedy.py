import linecache #lines are 1 indexed
import sys
import random
import re
import collections
#most





#only call this on lines in the matrix. will err otherwise.
def convert(file_name, node_index):
	"""turn line into list"""
	line = linecache.getline(file_name, node_index+1)
	line = line[2:line.index('\n')]
	line = line.split()
	line = [int(i) for i in line]
	return line



#current issue: if more than one node with same cost, only chooses first one
def cheapest(file_name, node, repeat, visited):
	for_index = convert(file_name, node)
	possibilities = []

	# print for_index
	# print node

	colors = linecache.getline(file_name, len(for_index)+2)
	color = for_index[node-1]



	if repeat == 3:
		for i in len(for_index):
			if (color != colors[i]) and (i+1 not in visited) and (i != node-1):
				possibilities.append((for_index[i], i)) #tuple of cost and index
	else:
		for i in range(len(for_index)):
			if (i+1 not in visited) and (i != node-1):
				possibilities.append((for_index[i], i))

	# print "possibilities: ", possibilities

	if possibilities == []:
		return False

	# print [min(possibilities)[0], min(possibilities)[1]+1]
	return [min(possibilities)[0], min(possibilities)[1]+1]


def greedy(file_name, N):
	# size = int(x) for x in f.readline().split() #read first line - size
	# starting_nodes = range(1, size+1) #list (0, ..., size-1)
	"""cheapest(file_name, node, repeat, visited)
	returns the cost and index of where to travel next """
	# print N
	# print type(N)
	curr_node = random.randrange(1, N+1) #initialize next as random variable
	# print curr_node

	return_path = [curr_node]
	visited = [curr_node]

	color_list = linecache.getline(file_name, N+2)
	repeat_colors = 1 #can't be greater than 3
	curr_color = color_list[curr_node]

	permute = range(1, N+1)

	while collections.Counter(return_path) != collections.Counter(permute):
		costs = convert(file_name, curr_node) #outgoing edge weights for current node
		if cheapest(file_name, curr_node, 1, visited):
			(choice_cost, choice) = cheapest(file_name, curr_node, 1, visited)
			choice_color = color_list[choice-1]
			# visited.append(choice)

		#need to backtrack
		else:
			curr_node = return_path[len(return_path)-3] #backtrack 2
			repeat_colors = 1
			(choice_cost, choice) = cheapest(file_name, curr_node, 1, visited)
			choice_color = curr_color
			visited = [i for i in visited[:len(visited-2)]]
			return_path = [i for i in return_path[:len(return_path-2)]]
			continue

		if choice_color == curr_color: 
			repeat_colors += 1
		else:
			repeat_colors = 0

		return_path.append(choice)
		visited.append(choice)

		curr_node = choice
		curr_color = color_list[choice-1]
	a = str(return_path)
	print re.sub('[^0-9]', ' ', str(a))
	for i in return_path:
		print color_list[i-1]
	return return_path
			
# greedy('4x4', 4)



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



