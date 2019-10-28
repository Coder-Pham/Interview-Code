"""
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return self.find(nums1, nums2)
        else:
            return self.find(nums2, nums1)

    def find(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        min_index = 0
        max_index = n
        median = 0

        while min_index <= max_index:
            i = int((min_index + max_index) / 2)
            j = int((n + m + 1) / 2 - i)

            if i < n and j > 0 and nums2[j - 1] > nums1[i]:
                min_index = i + 1
            elif i > 0 and j < m and nums2[j] < nums1[i - 1]:
                max_index = i - 1
            else:
                if i == 0:
                    median = nums2[j - 1]
                elif j == 0:
                    median = nums1[i - 1]
                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                break

        if (n + m) % 2 == 1:
            return median
        if i == n:
            return (median + nums2[j]) / 2
        if j == m:
            return (median + nums1[i]) / 2
        return (median + min(nums1[i], nums2[j])) / 2
