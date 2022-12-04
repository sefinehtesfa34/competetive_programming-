class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        for coin in coins:
            for target in range(1, amount + 1):
                if coin <= target:
                    dp[target] = min(dp[target], 1 + dp[target - coin])
        return dp[amount] if dp[amount] < amount + 1 else - 1
    
    