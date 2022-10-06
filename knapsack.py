from cmath import inf
class Solution:
    def knapsack(self, capacity, weights, values):
        def dp(index, capacity, value = 0, path = []):
            if capacity == 0:
                return (value, path)
            if index == len(weights):
                return (value, path)
            if weights[index] > capacity:
                return (value, path)
            take = dp(index + 1, 
                    capacity - weights[index], 
                    value + values[index], 
                    path + [index + 1])
            notTake = dp(index + 1, capacity, value, path)
            return max(take, notTake)
        return dp(0, capacity)
            
solution = Solution()
capacity = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
result = solution.knapsack(capacity, weights, values)
print(result)

dp = [[0]*(capacity + 1) for _ in range(len(weights) + 1)]
for index in range(1, len(weights) + 1):
    for cap in range(1, capacity + 1):
        if weights[index - 1] > cap:
            dp[index][cap] = dp[index - 1][cap]
        else:
            dp[index][cap] = max(dp[index - 1][cap], values[index - 1] + dp[index - 1][cap - weights[index - 1]])
print(dp[index][cap])
'''
   [0] [1] [2] [3] [4] [5] [6] [7]
[ ] 0   0   0   0   0   0   0   0  
[4] 0   0   0   0
[3] 0   0   0   2
[2] 0   0   4   
[3] 0   0   4
'''