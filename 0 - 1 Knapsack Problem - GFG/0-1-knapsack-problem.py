#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W,wt,val, n):
        dp = [[0]*(n + 1) for _ in range(W + 1)]
        
        for weight in range(1, W + 1):
            for index in range(1, n + 1):
                if wt[index - 1] <= weight:
                    dp[weight][index] = max(val[index - 1] + dp[weight - wt[index - 1]][index - 1], dp[weight][index])

                dp[weight][index] = max(dp[weight][index], dp[weight][index - 1])
        return dp[W][n]
        
                
                    
                    
        
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends