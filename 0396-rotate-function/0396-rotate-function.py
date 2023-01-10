class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        sums = sum(nums)
        cur_total = 0
        n = len(nums)
        for index in range(len(nums)):
            cur_total += index*nums[index]
        max_score = cur_total
        for index in range(len(nums)-1, -1, -1):
            cur_total -= nums[index]*(n - 1)
            cur_total += sums - nums[index]
            max_score = max(max_score, cur_total)
        return max_score
    
        
        
        
        
        
        
        
        
        