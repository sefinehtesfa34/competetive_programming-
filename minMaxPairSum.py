class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        for i in range(len(nums)//2):
            l.append(nums[i:i+1][0]+nums[len(nums)-1-i:len(nums)-i][0])
        return max(l)