import linecache #lines are 1 indexed
import sys
import random
import re

def cheapest(file_name, node, order):
	n = 1
	local_current = []
	line = re.sub('[^0-9]', '', linecache.getline(file_name, node+1))


	# print line

	local_current = [int(x) for x in line] #lines are 1-indexed
	
	# print local_current

	local_current.remove(min(local_current)) #gets rid of middle 0
	print local_current
	while n < order:
		local_current.remove(min(local_current))
		print n, "\n", order
		n+=1
	return min(local_current)



def greedy(file, file_name, N):
	# size = int(x) for x in f.readline().split() #read first line - size
	# starting_nodes = range(1, size+1) #list (0, ..., size-1)
	curr_node = random.randrange(1, N+1) #initialize next as random variable

	# print curr_node

	return_path = []
	color_list = linecache.getline(file_name, N+2)
	repeat_colors = 1 #can't be greater than 3
	curr_color = linecache.getline(file_name, N+2)[curr_node-1]

	while len(return_path) < N:
		current_list = []

		# print linecache.getline(file_name, curr_node+1)
		line = re.sub('[^0-9]', '', linecache.getline(file_name, curr_node+1))
		# print line


		current_list = [int(x) for x in line] #outgoing edge weights for current node
		choice_cost = cheapest(file_name, curr_node, 1)
		
		#tiebreaker if multiple edges with cheapest cost
		cheapest_indices = [i for i, x in enumerate(current_list) if x == choice_cost]

		# print curr_node
		# print curr_node
		# print cheapest_indices

		if curr_node in cheapest_indices:
			cheapest_indices.remove(curr_node)
		choice = current_list[cheapest_indices[random.randrange(0, len(cheapest_indices))]]

		choice_color = color_list[choice-1]

		#LOOP - if next move is an illegal color, get second cheapest
		if repeat_colors == 3:
			i = 2
			while choice_color == curr_color:
				choice_cost = cheapest(file_name, curr_node, i)
				cheapest_indices = [i for i, x in enumerate(current_list) if x == choice_cost]
				# print cheapest_indices
				# cheapest_indices.remove(curr_node-1)
				choice = current_list[cheapest_indices[random.randrange(0, len(cheapest_indices))]]
				choice_color = colors[choice - 1]
				i += 1
		if choice_color == curr_color: 
			repeat_colors += 1
		else:
			repeat_colors = 0
		return_path.append(choice)
		curr_color = color_list[choice-1]
			

	# visited_nodes.append(next) #for backtracking & forward checking
	# visited_reds = 0 #for later
	# visited_blues = 0 #for later
	#start from random node
	# for line in f:
	# return_path.append(start_node)
	# current.append([int(x) for x in linecache.getline(input_file, start_node+1)])
	# cheapest = min(current) #from random node, what's cheapest edge
	# next = current.index(cheapest) #next node to visit






# fin = open('4x4', 'r')
# greedy(fin, '4x4', 4)



T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline()) #size
    d = [[] for i in range(N)] #turn each row into array of integers
    for i in xrange(N):
        d[i] = [int(x) for x in fin.readline().split()]
    c = fin.readline() #print out row 

    # find an answer, and put into assign
    # assign = [0] * N
    assign = greedy(fin, str(t) + ".in", N) #call greedy strategy
    for i in xrange(N):
        assign[i] = i+1

    fout.write("%s\n" % " ".join(map(str, assign)))
fout.close()



