class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cur_end = 0
        for index in range(len(nums)):
            if index > cur_end:
                return False
            cur_end = max(cur_end, index + nums[index])
            
        return cur_end >= len(nums) - 1
            