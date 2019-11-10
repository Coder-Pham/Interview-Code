"""
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. 
For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. 
For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Goal: O(1) space complexity, O(n) time complexity
"""

def bracket_match(text):
  countOpen, countClose = 0, 0
  for x in text:
    if x == '(':
      countOpen += 1
    else:
      if countOpen == 0:
        countClose += 1
      else:
        countOpen -= 1
  return countOpen + countClose