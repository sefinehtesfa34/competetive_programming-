#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # code here 
        dp = [0]*(Sum + 1)
        dp[0] = 1
        for coin in coins:
            for cur in range(1, Sum + 1):
                if cur >= coin:
                    dp[cur] += dp[cur - coin]
        return dp[Sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends