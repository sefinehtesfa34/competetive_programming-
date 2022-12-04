class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        max_len = 0
        for index in range(len(s)):
            if index == 0:
                continue
            if s[index] == ')' and s[index - 1] == '(':
                dp[index] = 2 + (dp[index - 2] if index >= 2 else 0)
            elif s[index] == ')' and s[index - 1] == ')':
                if index == dp[index - 1]:
                    continue
                if s[index - dp[index - 1] - 1] == '(':
                    dp[index] = 2 + dp[index - 1] + (dp[index - dp[index - 1] - 2] 
                                                     if index - dp[index - 1] >= 2 else 0)
            max_len = max(max_len, dp[index])
        return max_len
    