class Solution:
    def distinctSubseqII(self, s: str) -> int:
        last = {}
        dp = [1]
        mod = 1000_000_007
        for index, char in enumerate(s):
            dp.append(dp[-1]*2)
            if char in last:
                dp[-1] -= dp[last[char]]
            last[char] = index
        return (dp[-1] - 1) % mod
    