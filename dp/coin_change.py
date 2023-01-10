class Solution:
    def coinChange(self):
        target = int(input())
        coins = list(map(int, input().split()))
        answer = []
        
        dp = [target + 1]*(target + 1)
        dp[0] = 0
        for curr in range(1, target + 1):
            for coin in coins:
                if coin <= curr :
                    dp[curr] = min(dp[curr], 1 + dp[curr - coin])
        
        
        
        curr = target
        while curr > 0:
            cur_coin = 0
            curr_count = 100_000
            for coin in coins:
                if coin <= curr:
                    if dp[curr - coin] < curr_count:
                        curr_count = dp[curr - coin]
                        cur_coin = coin
            curr -= cur_coin 
            answer.append(cur_coin)    
        print(answer)
        
solution = Solution()
result = solution.coinChange()
print(result)