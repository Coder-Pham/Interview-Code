'''
    Link: https://leetcode.com/problems/largest-number/
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums.sort(key = lambda x: x / 10 ** (len(str(x))-1), reverse=True)
        # nums.sort(key = lambda x: str(x), reverse=True) 
        class Predicate(str):
            def __lt__(self, other):
                return self + other < other + self

        strs = ''.join(sorted(map(str, nums), key=Predicate, reverse=True))
        return '0' if strs[0] == '0' else strs