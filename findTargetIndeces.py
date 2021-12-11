class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
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
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
        
                
                