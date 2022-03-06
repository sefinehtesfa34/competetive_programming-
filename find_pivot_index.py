class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        value1=[]
        val1=0
        value2=[]
        val2=0
        for i in range(len(nums)):
            val1+=nums[i]
            value1.append(val1)
            val2+=nums[len(nums)-1-i]
            value2.append(val2)
        i=0
        for val1,val2 in zip(value1,value2[::-1]):
            if (val1-nums[i])==(val2-nums[i]):
                return i
            i+=1
        return -1
            
