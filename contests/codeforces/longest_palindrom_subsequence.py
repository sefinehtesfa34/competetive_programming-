from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return 2 + dp(left + 1, right - 1)
            return max(dp(left + 1, right),dp(left, right - 1))
        return dp(0, len(s)-1)
    