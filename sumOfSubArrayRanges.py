class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        output=0
        for i in range(len(nums)):
            max_val=nums[i]
            min_val=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]<min_val:
                    min_val=nums[j]
                if nums[j]>max_val:
                    max_val=nums[j]
                output+=max_val-min_val
        return output
