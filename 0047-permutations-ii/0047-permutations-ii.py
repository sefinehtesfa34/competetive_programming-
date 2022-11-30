class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        chosen = Counter(nums)
        answer = []
        def backtrack(temp):
            if len(temp) == len(nums):
                answer.append(list(temp))
                return
            for curr in chosen:
                if chosen[curr] > 0:
                    chosen[curr] -= 1
                    temp.append(curr)
                    backtrack(temp)
                    chosen[curr] += 1
                    temp.pop()
        backtrack([])
        
        return answer
    