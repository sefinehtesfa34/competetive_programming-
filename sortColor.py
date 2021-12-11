class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            mn=nums[i]
            index=i
            for j in range(i+1,len(nums)):
                if nums[j]<mn:
                    mn=nums[j]
                    index=j
            val=nums[i]
            nums[i]=nums[index]
            nums[index]=val