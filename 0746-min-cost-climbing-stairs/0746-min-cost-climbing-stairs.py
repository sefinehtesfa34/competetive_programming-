class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost) + 1)
        dp[1] = cost[1] 
        for index in range(1, len(cost) + 1):
            dp[index] = cost[index - 1] + min(dp[index - 1], dp[index - 2])
        return min(dp[-1], dp[-2])
    
        