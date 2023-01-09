class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        for index in range(len(strs)):
            strs[index] = " " + strs[index]
        answer = 0
        n = len(strs[0])
        @cache
        def dp(index, prev):
            if index == n:
                return 0
            is_valid = True
            if not all(word[prev] <= word[index] for word in strs):
                is_valid = False
            pick = dp(index + 1, index) if is_valid else inf
            notPick = 1 + dp(index + 1, prev) 
            return min(pick, notPick)
        return dp(0, 0)
    