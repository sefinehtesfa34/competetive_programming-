class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        left = 1
        right = 2
        while right < len(nums):
            if nums[left - 1] != nums[left]:
                left += 1
            nums[left] = nums[right]
            right += 1
        return left + 1 if nums[left - 1] != nums[left] else left
    
    
    
            