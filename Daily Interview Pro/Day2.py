'''
  Problem: Find length of the longest substring without repeating characters.
  From: Microsoft
  Complexity: O(n)
'''

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    start = 0
    end = 0
    maxLen = 0
    uniqueChar = set()
    while start < len(s):
      while end < len(s) and s[end] not in uniqueChar:
        uniqueChar.add(s[end])
        end += 1
      maxLen = max(maxLen, len(uniqueChar))
      if end == len(s):
        maxLen = max(maxLen, len(uniqueChar))
        return maxLen
      else:
        while s[end] in uniqueChar:
          uniqueChar.remove(s[start])
          start += 1
    return maxLen

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))