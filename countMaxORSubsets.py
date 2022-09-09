from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result = 0
        max_or = 0
        for num in nums:
             max_or |= num
        def backtrack(index,cur_or):
            nonlocal result
            if cur_or == max_or:
                result += 1
            for begin in range(index,len(nums)):
                backtrack(begin + 1, cur_or | nums[begin])
        backtrack(0,0)
        return result
    
            