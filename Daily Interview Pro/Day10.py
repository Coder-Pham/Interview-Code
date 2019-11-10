'''
Given an integer k and a binary search tree, find the floor (less than or equal to) of k, 
and the ceiling (larger than or equal to) of k. 
If either does not exist, then print them as None.

From: Apple
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k):
    # Find the node has value k
    # floor value = Max node of left tree of that node
    # Ceil value = Min node of right tree of that node
    return (Floor(root_node, k), Ceil(root_node, k))

def Ceil(root, key):
    if root == None:
        return None
    elif root.value == key:
        return root.value
    elif root.value > key:
        ceilValue = Ceil(root.left, key)
        return ceilValue if ceilValue != None else root.value
    elif root.value < key:
        return Ceil(root.right, key)

def Floor(root, key):
    if root == None:
        return None
    elif root.value == key:
        return root.value
    elif root.value > key:
        return Floor(root.left, key)
    elif root.value < key:
        floorValue = Floor(root.right, key)
        return floorValue if floorValue != None else root.value

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)
