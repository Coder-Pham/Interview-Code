'''
Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
Assume the expression is properly formed.

From: Google

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
'''

def eval(expression):
	numStack = []
	opStack = []

	if expression[0] == '-':
		numStack.append(0)

	
	for x in expression:
		if x == '-' or x == '+':
			opStack.append(x)
		elif x.isdigit():
			numStack.append(int(x))
		elif x == '(':
			opStack.append(x)
		elif x == ')':
			while len(opStack) != 0 and opStack[-1] != '(':
				op = opStack.pop()
				num1 = numStack.pop()
				num2 = numStack.pop()
				if op == '-':
					numStack.append(num2 - num1)
				else:
					numStack.append(num2 + num1)
			opStack.pop()

	while len(opStack) != 0:
		op = opStack.pop()
		num1 = numStack.pop()
		num2 = numStack.pop()
		if op == '-':
			numStack.append(num2 - num1)
		else:
			numStack.append(num2 + num1)
	return numStack.pop()


print(eval('- (3 + ( 2 - 1 ) )'))
# -4
