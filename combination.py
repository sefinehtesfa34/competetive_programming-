# class Solution:
#     def combination(self, n, m):
#         if n == m or n == 0 or m == 0:
#             return 1
#         return self.combination(n - 1, m) + self.combination(n - 1, m - 1)
# solution = Solution()
n, m = list(map(int, input().split()))
# result = solution.combination(n, m)
# print(result)
dp = [[0]*(m + 1) for _ in range(n + 1)]
for index in range(min(n, m) + 1):
    dp[index][index] = 1
    dp[index][0] = 1
    dp[0][index] = 1
for index in range(1, n + 1):
    for cur in range(1, min(index, m + 1)):
        if index == cur :
            break 
        dp[index][cur] = dp[index - 1][cur] + dp[index - 1][cur - 1]
        
print(dp[n][m])
print(dp)


'''
[[1, 1, 1], 
[1, 1, 0], 
[1, 2, 1], 
[0, 3, 3], 
[0, 3, 6]]

'''


    
# print(dp[n][m])



'''
dp = [[0]*(m + 1) for _ in range(n + 1)]
# for index in range(n + 1):
#     dp[index][0] = 1
#     for cur in range(index):
#         dp[0][cur] = 1
#         if cur == index:
#             dp[index][cur] = 1
#             break
#         dp[index][cur] = dp[index - 1][cur] + dp[index - 1][cur - 1]
# return dp[n][m]

            
        



  1 2 3 4
  4 * 3 * 2! /2! * 2!
                                        c(4, 2)
                                      /        \
                             c(3, 2)   +         c(3, 1)
                            /        \           /      \
                        c(2, 2)   +   c(2, 1)  c(2, 2) + c(2, 1)
                                      /    \               /  \
                                  c(2, 0) + c(1, 0)  c(2, 0) + c(1, 0)
                                  
                
             
            
c(1, 2) = 1 + 1 = 2
c(1, 1) = 1 + 1 = 2
c(2, 1)  = 1 + 1 = 2
c(2, 2) = 1
c(3, 1) = c(2, 2) + c(2, 1) = 1 + 2 = 3
c(3, 2) = c(2, 2) + c(2, 1) = 1 + 2 = 3
c(4, 2) = c(3, 2) + c(3, 1) = 3 + 3 = 6

return 4
                             
  
 
'''

