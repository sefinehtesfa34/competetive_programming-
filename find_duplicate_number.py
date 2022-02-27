class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while True:
            num=nums[0]
            if num==nums[num]:
                return num
            nums[0],nums[num]=nums[num],num
            
            
            
        
        
