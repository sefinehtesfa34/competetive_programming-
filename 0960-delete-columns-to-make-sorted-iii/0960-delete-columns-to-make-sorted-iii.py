class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1] * len(strs[0])
        n = len(strs[0])
        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                if all(word[left] <= word[right] for word in strs):
                    dp[left] = max(dp[left], 1 + dp[right])
        return n - max(dp)
    