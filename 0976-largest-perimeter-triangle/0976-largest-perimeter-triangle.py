class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        answer = 0
        left = 0
        right = 2
        while right < len(nums):
            if sum(nums[left: left + 2]) > nums[right]:
                answer = sum(nums[left:right + 1])
            left += 1
            right += 1
        return answer
    
            