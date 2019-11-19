'''
Given two strings, determine the edit distance between them. 
The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

From: AirBnB

Topic: Longest Common Subsequence
'''


def distance(s1, s2):
    n = len(s1)
    m = len(s2)
    lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                lcs[i + 1][j + 1] = lcs[i][j] + 1
            else:
                lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i+1][j])

	# Number of letter need to add more
	# we only add more letter to the shorter string, when 2 strings are equal
	# We calculate number of the letter need to change
	# By the shortcut, change letter + add letter = longest - lcs
    return max(n, m) - lcs[n][m]


print(distance('biting', 'sitting'))
# 2
