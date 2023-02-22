class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = zeros = 0
        for index in range(len(s)):
            zeros += 1 if s[index] == '0' else 0
            ans = max(ans + 1, zeros) if zeros > 0 and s[index] == '1' else ans
        return ans
    