
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0]*(1 + len(S1)) for _ in range(1 + len(S2))]
        longest = 0
        for index in range(1, len(S2) + 1):
            for cur in range(1, len(S1) + 1):
                if S1[cur - 1] == S2[index - 1]:
                    dp[index][cur] = 1 + dp[index - 1][cur - 1]
                longest = max(longest, dp[index][cur])
        return longest
