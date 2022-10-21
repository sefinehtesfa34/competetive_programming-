from cmath import inf
from typing import Counter
class Solution:
    def coin_change(self):
        coins = self.get_coins()
        target = self.get_target()
        #Building a two dimensional grid for calculating the minimum number of coins
        # that give me the target.
        dp = [inf]*(target + 1)
        
        # If the target is zero, we don't need any coin to make it.
        dp[0] = 0
        # Calculating the minimum number of coins.
        first = [0]*(target + 1)
        for curr_target in range(1, target + 1):
            for coin in coins:
                if curr_target - coin >=0 and dp[curr_target - coin] + 1 < dp[curr_target]:
                    dp[curr_target] = dp[curr_target - coin] + 1
                    first[curr_target] = coin
        # Print the path of coins that give us a target sum of coins.
        n = target 
        while n > 0:
            print(first[n], end = ' ')
            n -= first[n]
        return print('\n', dp[target])
        
    
    def get_target(self):
        return int(input())
    def get_coins(self):
        return list(map(int, input().split()))
solution = Solution()
solution.coin_change()
