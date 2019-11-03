'''
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. 
Return -1 if the target is not found.

From: AirBNB

ex:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''


class Solution:
    def getRange(self, arr, target):
        i, j = 0, len(arr) - 1
        while i <= j:
            if arr[i] != target:
                i += 1
            if arr[j] != target:
                j -= 1
            if arr[i] == arr[j] == target:
                return [i, j]
        return [-1, -1]


# Test program
arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
# [1, 4]
