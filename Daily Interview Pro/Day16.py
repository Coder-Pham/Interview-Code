'''
Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
'''

def findSequence(seq):
	sequence = []
	maxLen = 0
	first, last = 0, 0
	while last < len(seq):
		if (seq[last] in sequence and len(set(sequence)) <= 2) or (seq[last] not in sequence and len(set(sequence)) < 2):
			sequence.append(seq[last])
			last += 1
		else:
			maxLen = max(maxLen, last - first)
			while len(set(sequence)) == 2:
				sequence.pop(0)
				first += 1
	return max(maxLen, last - first)

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
