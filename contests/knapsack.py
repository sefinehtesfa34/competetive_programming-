#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W,wt,val, n):
        dp = [[0]*(n + 1) for _ in range(W + 1)]
        
        for weight in range(1, W + 1):
            for index in range(1, n + 1):
                
                take = val[index - 1] + dp[weight - wt[index - 1]][index - 1] if wt[index] <= weight else 0
                not_take = dp[weight][index - 1]
                dp[weight][index] = max(take, not_take)
                
                
        return dp[W][n]
        