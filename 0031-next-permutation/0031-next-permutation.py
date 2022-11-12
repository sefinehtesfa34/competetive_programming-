
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left):
            right = len(nums) - 1
            left = max(0, left)
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return 
                
        right = len(nums) - 1
        left = right - 1
        while left >= 0 and nums[left] >= nums[right]:
            left -= 1
            right -=1
        if left < 0:
            return reverse(left)
        
        right = len(nums) - 1
        while right >= 0 and nums[right] <= nums[left]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        return reverse(left + 1)
        
        