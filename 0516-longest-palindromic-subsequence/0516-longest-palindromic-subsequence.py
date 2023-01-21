class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s) + 1) for _ in range(len(s) + 1)]
        for index in range(len(s)):
            dp[index][index] = 1
        max_len = 1
        for left in range(len(s)):
            for right in range(len(s)-1, -1, -1):
                if right < left:
                    break
                if right == left:
                    dp[left][right] = 1 + dp[left - 1][right + 1]
                elif s[left] == s[right]:
                    dp[left][right] = 2 + dp[left - 1][right + 1]
                else:
                    dp[left][right] = max(dp[left - 1][right], dp[left][right + 1])
                max_len = max(max_len, dp[left][right])
        return max_len