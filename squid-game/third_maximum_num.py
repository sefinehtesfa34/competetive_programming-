class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        first = second = third = -inf
        for num in nums:
            third = max(third, min(first, second, num))
            second = max(second, min(first, num))
            first = max(first, num)
        return third if third != -inf else first
    
        
        
        