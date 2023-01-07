class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices) + 1)]
        # dp[index][0] = buy at index day
        # dp[index][1] = sell at index day
        dp[0][0] = -prices[0]
        max_result = 0
        for index in range(1, len(prices)):
            dp[index][0] = max(-prices[index] + dp[index - 2][1], dp[index - 1][0])
            dp[index][1] = max(prices[index] + dp[index - 1][0], dp[index - 1][1])
            max_result = max(max_result, dp[index][0], dp[index][1])
        return max_result