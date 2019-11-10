'''
Implement a class for a stack that supports all the regular functions (push, pop) and an additional function 
of max() which returns the maximum element in the stack (return None if the stack is empty). 
Each method should run in constant time.

From: Twitter
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.maxStack) == 0:
            self.maxStack.append(val)
        else:
            self.maxStack.append(max(val, self.maxStack[-1]))

    def pop(self):
        self.stack.pop()
        self.maxStack.pop()

    def max(self):
        return self.maxStack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
