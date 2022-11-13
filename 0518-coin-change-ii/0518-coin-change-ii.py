class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
#         @cache
#         def dp(index, amount):
#             if amount == 0:
#                 return 1
#             if amount < 0 or index == len(coins):
#                 return 0
#             # count = 0
#             # for curr in range(index, len(coins)):
#                 # count += dp(curr, amount - coins[curr])
#             return dp(index, amount - coins[index]) + dp(index + 1, amount)
        
#         return dp(0, amount)

        dp = [[0]*(len(coins) + 1) for _ in range(amount + 1)]
        for index in range(len(coins) + 1):
            dp[0][index] = 1
        
        for curr_amount in range(1, amount + 1):
            for index in range(1, len(coins) + 1):
                dp[curr_amount][index] = dp[curr_amount][index - 1]
                if coins[index - 1] <= curr_amount:
                    dp[curr_amount][index] += dp[curr_amount - coins[index - 1]][index]
        return dp[amount][len(coins)]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    