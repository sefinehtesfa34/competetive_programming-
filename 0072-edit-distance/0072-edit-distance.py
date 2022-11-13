class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        for index in range(len(dp[0])):
            dp[0][index] = index
        for index in range(len(dp)):
            dp[index][0] = index
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])
        return dp[n][m]
    
        