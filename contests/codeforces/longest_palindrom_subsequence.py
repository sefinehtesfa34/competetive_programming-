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
    
solution = Solution()
s = input()
result = solution.longestPalindromeSubseq(s)
print(result)
dp = [[0]*(len(s) + 1) for _ in range(len(s) + 1)]
for left in range(1, len(s) + 1):
    for right in range(len(s) - 1, -1, -1):
        if left == right:
            dp[left][right] = 1
            break 
        elif s[left - 1] == s[right]:
            dp[left][right] = 2 + dp[left - 1][right + 1]
        else:
            dp[left][right] = max(dp[left - 1][right], dp[left][right + 1])
print(dp)
print(dp[len(s) - 1][0])
'''

[[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 2, 2, 2, 2, 0, 0], 
[0, 0, 1, 4, 4, 2, 2, 0], 
[0, 0, 0, 1, 4, 4, 2, 0], 
[0, 0, 0, 0, 1, 4, 2, 0], 
[0, 0, 0, 0, 0, 1, 2, 0], 
[0, 0, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]]

0 1 0 1 0 1
  
'''