'''
You are given a 2D array of characters, and a target string. 
Return whether or not the word target word exists in the matrix. 
Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

From: Amazon

Example:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
'''
import queue

direction = [[1, 0], [0, 1]]

def check(x, y, n, m):
	if 0 <= x < n and 0 <= y < m:
		return True
	return False

def BFS(x, y, idx, n, m, matrix, word):
	q = queue.Queue()
	visited = [[False for _ in range(m)] for _ in range(n)]
	q.put((x, y, idx))
	while not q.empty():
		ux, uy, i = q.get()
		for direct in direction:
			vx, vy = ux + direct[0], uy + direct[1]
			if check(vx, vy, n, m) and not visited[vx][vy] and matrix[vx][vy] == word[i + 1]:
				q.put((vx, vy, i + 1))
				visited[vx][vy] = True
				if i + 1 == len(word) - 1:
					return True
	

def word_search(matrix, word):
    # Fill this in.
	n = len(matrix)
	m = len(matrix[0])
	result = False
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == word[0]:
				if BFS(i, j, 0, n, m, matrix, word):
					result = True
	return result

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True
