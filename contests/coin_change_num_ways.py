from cmath import inf
from typing import Counter
class Solution:
    def coin_change(self):
        coins = self.get_coins()
        target = self.get_target()
        count = [0]*(target + 1)
        
        # If the target is zero, we have got one possible path.
        count[0] = 1
        for curr_target in range(1, target + 1):
            for coin in coins:
                if curr_target - coin >=0:
                    count[curr_target] += count[curr_target - coin]
                    count[curr_target] %= (10**9 + 7)
        return print('\n', count[target])
        
    def get_target(self):
        return int(input())
    def get_coins(self):
        return list(map(int, input().split()))
solution = Solution()
solution.coin_change()
