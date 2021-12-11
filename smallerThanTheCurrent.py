class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        count=0
        for i in range(len(nums)):
            num=nums[i]
            for j in range(len(nums)):
                if i!=j:
                    if nums[j]<num:
                        count+=1
            l.append(count)
            count=0
        return l