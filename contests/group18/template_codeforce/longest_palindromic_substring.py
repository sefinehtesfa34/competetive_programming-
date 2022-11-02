class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cur_max = 1
        dp = [[0]*(len(s) + 1) for _ in range(len(s) + 1)]
        for left in range(1, len(s) + 1):
            dp[left][left] = 1
            for right in range(left - 1 , 0, -1):
                if s[left - 1] == s[right - 1]:
                    dp[left][right] = 2 + dp[left - 1][right + 1]
                else:
                    dp[left][right] = max(dp[left][right + 1], dp[left - 1][right])
                cur_max = max(dp[left][right], cur_max)
        return cur_max
    
    
    
    