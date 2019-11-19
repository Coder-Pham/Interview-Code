'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

From: Amazon
'''

class Solution:
	def minSubArrayLen(self, nums, s):
		currSum = 0
		cumSum = [0]
		for x in nums:
			currSum += x 
			cumSum.append(currSum)

		if cumSum[-1] < s:
			return 0

		first, last = 0, 1
		minLen = 10**9
		while first < len(cumSum):
			if last == len(cumSum):
				break
			if cumSum[last] - cumSum[first] < s:
				last += 1
			else:
				minLen = min(minLen, last - first)
				first += 1
		return minLen

# [0, 2, 5, 6, 8, 12, 15]
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
