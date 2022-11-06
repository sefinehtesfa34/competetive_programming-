class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[0] = 1
        for index in range(1, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]
        return dp[n]
    
    
    