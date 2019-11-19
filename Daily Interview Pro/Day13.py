'''
Given a list of numbers, find if there exists a pythagorean triplet in that list. 
A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

From: Uber

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
'''

def findPythagoreanTriplets(nums):
    # Fill this in.
	power2 = set()
	for x in nums:
		power2.add(x**2)
	
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			if (nums[i]**2 + nums[j]**2) in power2:
				return True
	return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
