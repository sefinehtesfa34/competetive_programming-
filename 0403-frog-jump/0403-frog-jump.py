class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] > 1:
            return False
        
        @cache
        def dp(index, jump):
            if index == len(stones):
                return False
            if index == len(stones) - 1:
                return True
            answer = False
            for curr in range(index + 1, len(stones)):
                if stones[curr] - stones[index] > jump + 1:
                    return answer
                for step in range(-1, 2):
                    if stones[curr] - stones[index] == jump + step:
                        answer = answer or dp(curr, jump + step)
                
            return answer
        
        return dp(1, 1)
    
                
            