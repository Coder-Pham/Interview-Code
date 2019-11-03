'''
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

From: Google
'''

def sortNums(nums): # Return a sorted list
  # Fill this in. 
	count1, count2, count3 = 0, 0, 0
	for x in nums:
		if x == 1:
			count1 += 1
		elif x == 2:
			count2 += 1
		elif x == 3:
			count3 += 1
	return [1] * count1 + [2]*count2 + [3]*count3	

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
