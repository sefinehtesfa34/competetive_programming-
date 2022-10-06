from functools import cache


class Solution:
    def editDistance(self, str1, str2):
        @cache
        def dp(str1ptr, str2ptr):
            if str1ptr == len(str1):
                return len(str2) - str2ptr
            if str2ptr == len(str2):
                return len(str1) - str1ptr
            if str1[str1ptr] == str2[str2ptr]:
                return dp(str1ptr + 1, str2ptr + 1)
            return 1 + min(dp(str1ptr + 1, str2ptr), dp(str1ptr, str2ptr + 1), dp(str1ptr + 1, str2ptr + 1))
        return dp(0, 0)
solution = Solution()
str1 = input()
str2 = input()
result = solution.editDistance(str1, str2)
print(result)
dp = [[0]*(len(str2) + 1) for _ in range(len(str1) + 1)]
for index in range(1, len(str1) + 1):
    dp[index][0] = index
for index in range(1, len(str2) + 1):
    dp[0][index] = index
for index in range(1, len(str1) + 1):
    for cur in range(1, len(str2) + 1):
        if str1[index - 1] == str2[cur - 1]:
            dp[index][cur] = dp[index - 1][cur - 1]
        else:
            dp[index][cur] = 1 + min(dp[index - 1][cur -1], dp[index - 1][cur], dp[index][cur - 1])
print(dp[len(str1)][len(str2)])

'''
[
[0, 1, 2], 
[1, 1, 2], 
[2, 2, 2], 
[3, 2, 3], 
[4, 3, 2], 
[5, 4, 3], 
[6, 5, 4], 
[7, 6, 5]
]


    [] [c] [o] [m] [p] [u] [t] [e] [r]
    ______________________________
[]   0  1   2   3   4  5   6   7  8
[c]| 1  0   1   2   3  4   5   6  7   
[o]| 2  1   0   1   2  3   4   5  6           
[m]| 3  2   1   0   1  2   3   4  5
[m]| 4  3   2   1   2  3   3   4  5
[u]| 5
[t]| 6
[e]| 7
[r]| 8







str1 = CAR
str2 = CAT                                                  dp(CAT, CAR)
                                                       /           |           \
                                                     dp(AT, CAR)   dp(CAT, AR)  dp(AT, AR)
                                                  /   |   \
                                                 /    |    \
                                                /     |     \
                                           THE HEIGHT OF THE TREE IS THE MINIMUM OF THE LENGTH OF THE 
                                           TWO STRINGS T = MIN(N, M)
                                           
                                           Time complexity: O(3*T)
                                           Space complexity: O(N)
                                           
                                           
                                                          



'''