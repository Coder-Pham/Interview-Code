'''
    Problem: You are given two linked-lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.

    From: Microsoft
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def convertNum(self, linklist):
        cnt = 0
        num = 0
        while linklist is not None:
            num += linklist.val * 10** cnt
            cnt += 1
            linklist = linklist.next 
        return num

    def convertList(self, num):
        lst = currentNode = ListNode(num % 10)
        num //= 10
        while num / 10 != 0:
            currentNode.next = ListNode(num % 10)
            num //= 10
            currentNode = currentNode.next
        return lst 

    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        total = self.convertNum(l1) + self.convertNum(l2)
        return self.convertList(total)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
