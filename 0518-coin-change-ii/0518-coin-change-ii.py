class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def dp(index,amount):
            if amount == 0: 
                return 1
            if amount < 0:
                return 0
            if index>=len(coins):
                return 0
            take = dp(index, amount - coins[index])
            dont_take = dp(index + 1, amount)
            return take + dont_take
        
        return dp(0, amount)
    
