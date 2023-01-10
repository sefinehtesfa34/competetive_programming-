from math import inf 
def dp(index, amount):
    if (index, amount) in memo:
        return memo[index, amount]
    if amount == 0:
        return 0
    if index == len(coins) or amount < 0:
        return inf
    
    memo[index, amount] = min(1 + dp(index + 1, amount - coins[index]), dp(index + 1, amount))
    return memo[index, amount]

memo = {}
coins = [1,2, 1, 5,4, 7]
print(dp(0, 4))
print(memo)
# cur_amount = 0
# index = len(coins) - 1
# amount = 16
# while cur_amount <= amount:
#     coin = 0
#     max_amount = cur_amount 
#     for curr in range(len(coins)):
#         if (curr, cur_amount) in memo and memo[curr, cur_amount] != inf:
#             max_amount = max(max_amount, cur_amount + coins[curr])
#     cur_amount = max_amount 
    
#     print(coin)
#     break
    
    
