class Solution:
    def __init__(self,N):
        self.memo = [-1] * (N + 1)
    def tripleStep(self,N):
        if N <= 1:
            return N 
        # if self.memo[N]!= -1:
        #     return self.memo[N]
        # if N == 0:
        #     return 1
        # if N < 0:
        #     return 0
        # oneJump = self.tripleStep(N - 1)
        # twoJump = self.tripleStep(N - 2)
        # threeJump = self.tripleStep(N - 3)
        # self.memo[N] = oneJump + twoJump + threeJump 
        # return self.memo[N]
        dp = [0]*(N + 1)
        dp[0] = 1
        for index in range(1,N + 1):
            dp[index] = dp[index - 3] + dp[index - 2] + dp[index - 1]
        return dp[N]
        # dp[0] = 1
        # dp[1] = dp[0] + dp[-1] + dp[-2] = 1 + 0 + 0 = 1
        # dp[2] = dp[1] + dp[0] + dp[-1] = 1 + 1 + 0 = 2
        # dp[3] = dp[0] + dp[1] + dp[2] = 1 + 1 + 2 = 4
        # dp[4] = dp[3] + dp[2] + dp[1] = 4 + 2 + 1 = 7
         
        
    
        
N = int(input())
solution = Solution(N)
result = solution.tripleStep(N)
print(result)
