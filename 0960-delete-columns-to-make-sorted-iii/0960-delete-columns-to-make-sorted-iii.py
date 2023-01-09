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
            for word in strs:
                if word[prev] > word[index]:
                    is_valid = False
                    break
            pick = dp(index + 1, index) if is_valid else inf
            notPick = 1 + dp(index + 1, prev) 
            return min(pick, notPick)
        
        return dp(0, 0)
    