class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(index, turn, k):
            if index == len(prices) or k == 0:
                return 0
            return max(-prices[index] + dp(index + 1, False, k), dp(index + 1, turn, k)) \
                if turn else max(dp(index + 1, turn, k), prices[index] + dp(index + 1, True, k - 1))
            
        return dp(0, True, k)
    
    
    
    