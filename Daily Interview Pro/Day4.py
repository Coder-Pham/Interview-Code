'''
Imagine you are building a compiler. 
Before running any code, the compiler must check that the parentheses in the program are balanced. 
Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

    From: Uber
'''


class Solution:
    def isValid(self, s):
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif brackets[stack[-1]] == s[i]:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
