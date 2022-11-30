class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        chosen = {index:False for index in range(len(nums))}
        answer = set()
        nums.sort()
        def backtrack(temp):
            if len(temp) == len(nums):
                answer.add(tuple(temp))
                return
            
            for curr in range(len(nums)):
                if chosen[curr] == False:
                    chosen[curr] = True
                    temp.append(nums[curr])
                    backtrack(temp)
                    chosen[curr] = False
                    temp.pop()
        backtrack([])
        
        return answer
    