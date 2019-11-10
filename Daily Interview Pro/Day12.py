'''
You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. 
Write a function that returns the number of unique ways to climb the stairs.

Should: O(n) time

From: Linkedln
'''

def staircase(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
  
print(staircase(4))
# 5
print(staircase(5))
# 8
print(staircase(10**4))
