def riverSizes(matrix):
	rivers = []
	visited = [[False for value in row] for row in matrix]

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if not visited[i][j]:
				traverse(i, j, matrix, visited, rivers)

	return rivers

def traverse(i, j, matrix, visited, rivers):
	current_river_size = 0
	nodes_to_traverse = [[i, j]]

	while nodes_to_traverse:
		current_node = nodes_to_traverse.pop()
		i = current_node[0]
		j = current_node[1]
		if not visited[i][j]:
			visited[i][j] = True
			if matrix[i][j] == 1:
				current_river_size += 1
				unvisited = getUnvisitedNeighbors(i, j, matrix, visited)
				for neighbor in unvisited:
					nodes_to_traverse.append(neighbor)

	if current_river_size > 0:
		rivers.append(current_river_size)

def getUnvisitedNeighbors(i, j, matrix, visited):
	unvisited = []
	if i > 0 and i < len(matrix) - 1:
		unvisited.append([i-1, j])
		unvisited.append([i+1, j])
	elif i == len(matrix) - 1:
		unvisited.append([i-1, j])
	elif i == 0:
		unvisited.append([i+1, j])
	if j > 0 and j < len(matrix[i]) - 1:
		unvisited.append([i, j-1])
		unvisited.append([i, j+1])
	elif j == len(matrix[i]) - 1:
		unvisited.append([i, j-1])
	elif j == 0:
		unvisited.append([i, j+1])
	return unvisited
