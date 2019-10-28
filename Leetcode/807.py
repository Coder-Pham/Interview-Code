'''
    Link: https://leetcode.com/problems/max-increase-to-keep-city-skyline/
'''
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        vertical = []
        horizontal = []
        n = len(grid)
        
#         Highest on each row
        for i in range(n):
            skyline = 0
            highest = 0
            for j in range(n):
                if highest < grid[i][j]:
                    highest = grid[i][j]
                    skyline = j
            horizontal.append(skyline)
            
#         Highest on each col
        for i in range(n):
            skyline = 0
            highest = 0
            for j in range(n):
                if highest < grid[j][i]:
                    highest = grid[j][i]
                    skyline = j
            vertical.append(skyline)
            
#         Calculate max sum
        totalSum = 0
        for i in range(n):
            for j in range(n):
                minHeight = min(grid[i][horizontal[i]], grid[vertical[j]][j])
                totalSum += minHeight - grid[i][j] 
        return totalSum