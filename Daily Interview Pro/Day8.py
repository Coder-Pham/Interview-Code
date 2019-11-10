'''
You are given a list of numbers, and a target number k. 
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.

From: Facebook
'''


def two_sum(lst, k):
    # Fill this in.
    check_exist = dict()
    for x in lst:
        check_exist[x] = check_exist.get(x, 1)
        if check_exist.get(k - x, 0):
            return True
    return False


print(two_sum([4, 7, 1, -3, 2], 5))
