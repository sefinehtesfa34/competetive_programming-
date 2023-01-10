class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*128
        for char in s:
            dp[ord(char)] += 1
            for pos in range(ord(char) - k, ord(char) + k + 1):
                if 97 <= pos <= 127 and pos != ord(char):
                    dp[ord(char)] = max(dp[ord(char)], 1 + dp[pos])
        return max(dp)
    