class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp  = [0]*(len(s) + 1)
        answer = 0
        for index, char in enumerate(s):
            if char == ')' and index > dp[index - 1] and s[index - dp[index - 1] - 1] == '(':
                dp[index] = 2 + dp[index - 1] + dp[index - dp[index - 1] - 2]
        return max(dp)
    