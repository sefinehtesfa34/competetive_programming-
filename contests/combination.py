# from math import *
# print(factorial(10000)//((factorial(1000)*factorial(10000 - 1000))))
class Solution:
    def combination(self):
        n, m = list(map(int, input().split()))
        
        # def comb(n, m):
        #     if n == m or m == 0 or n == 0:
        #         return 1
        #     return comb(n - 1, m) + comb(n - 1, m - 1) 
        
        # return print(comb(n, m))
    
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        
        for index in range(m):
            dp[0][index] = 1
            
        for index in range(n):
            dp[index][0] = 1
        
        for index in range(1, n + 1):
            for curr in range(1, min(m, index) + 1) :
                if index == curr:
                    dp[index][curr] = 1
                else:
                    dp[index][curr] = dp[index - 1][curr] + dp[index - 1][curr - 1]
        print(dp[n][m])
        
solution = Solution()
solution.combination()



