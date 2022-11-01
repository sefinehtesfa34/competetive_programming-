class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        for curr in range(amount + 1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr], 1 + dp[curr - coin])
        return dp[amount] if dp[amount] <= amount else -1
    
                                   
                                   
                                   
                                   