class Solution:
    def solve(self):
        score = int(input())
        dp = [0] * (score + 1)
        # dp [x] = dp[x - 3] + dp[x - 5 ] + dp[x - 10]
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        # 