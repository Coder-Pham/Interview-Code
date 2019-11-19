'''
You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

From: Microsoft
'''

def num_ways(n, m):
    # Create a matrix of n x m
    # for ways[i][j] is the number of ways from grid[0][0] to grid[i][j]
    ways = [[0 for _ in range(m)] for _ in range(n)]
    # Therefore, ways[i][0] = ways[0][j] = 1 because we can only by routes right or down
    for i in range(n):
        ways[i][0] = 1
    for j in range(m):
        ways[0][j] = 1

    # Also because only by go right or down so to go to grid[i][j], we must either go from grid[i-1][j] or grid[i][j-1] 
    # Therefore, number of ways to go to grid[i][j] is the sum of number of ways to grid[i-1][j] and grid[i][j-1]
    for i in range(1, n):
        for j in range(1, m):
            ways[i][j] = ways[i-1][j] + ways[i][j-1]
    # As the result, ways[n-1][m-1] is the number of ways to go from (0,0) to (n, m)
    return ways[n-1][m-1]
    

print(num_ways(2,3))
# 2
