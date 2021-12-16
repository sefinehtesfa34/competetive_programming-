class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for val in range(len(nums)-1):
            if val%2==1:
                temp=nums[val+1]
                nums[val+1]=nums[val]
                nums[val]=temp
        return nums