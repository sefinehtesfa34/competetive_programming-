# Top up approach dynamic programming
from functools import cache



class Solution:
    def reachAscore(self, N, memo = {}):
        if N < 3:
            return 0
        if N == 0:
            return 1
        memo[N] = self.reachAscore(N - 3) + self.reachAscore(N - 5) + self.reachAscore(N - 10)
        return memo[N]
solution = Solution()
N = int(input())
result = solution.reachAscore(N)
print(result)

# Bottom up approach of dynamic programming
# dp = [0]*(N + 1)
# dp[0] = 1
# for n in range(3, N + 1):
#     dp[n] = dp[n - 3] + dp[n - 5] + dp[n - 10]
# print(dp[N])


'''
                                  N = 20
                                      13
                                   /   |  \
                                  10    8  3
                                / | \  / | \
                               7  5  0 5 3 -2
                             / | \     
                            4  2  -3
                         /  | \
                        1   -5 -6 
'''                     