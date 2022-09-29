'''
Description
A subsequence of a string s is considered a good palindromic subsequence if:

It is a subsequence of s.
It is a palindrome (has the same value if reversed).
It has an even length.
No two consecutive characters are equal, except the two middle ones.
For example, if s = "abcabcabb", then "abba" is considered a good palindromic subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive characters) are not.

Given a string s, return the length of the longest good palindromic subsequence in s.

Example 1:

Input: s = “bbabab”

Output: 4
Explanation: The longest good palindromic subsequence of s is “baab”.

Example 2:

Input: s = “dcbccacdb”

Output: 4

Explanation: The longest good palindromic subsequence of s is “dccd”.

Constraints:

1 <= s.length <= 250
s consists of lowercase English letters.

'''
class Solution:
    def longestPSS(self,strs):
        def dfs(left, right, prev):
            if left >= right:
                return 0
            if strs[left] == strs[right] and strs[left] != prev:
                return 2 + dfs(left + 1, right - 1, strs[left])
            return max(dfs(left + 1, right, prev), dfs(left, right - 1, prev))
        return dfs(0, len(strs) - 1, '')
solution = Solution()
strs = input()
longest = solution.longestPSS(strs)
print(longest)

                
                
    