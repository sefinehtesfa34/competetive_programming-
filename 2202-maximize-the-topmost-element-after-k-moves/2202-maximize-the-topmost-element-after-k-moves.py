class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1 and k%2 == 1:
            return -1
        answer = -1
        index = 0
        while k > 1 and index < len(nums):
            answer = max(answer, nums[index])
            index += 1
            k-=1
        return max(answer, nums[index + 1] if index + 1 < len(nums) else -1) 
        
    
        
    
            
            
            