'''
    Problem: A palindrome is a sequence of characters that reads the same backwards and forwards. 
    Given a string, s, find the longest palindromic substring in s.

    From: Twitter
'''


class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        maxLen = 1
        start = 0
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if maxLen < j - i + 1:
                        maxLen = j - i + 1
                        start = i

        return s[start:start + maxLen]


# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
