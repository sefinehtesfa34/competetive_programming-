class Solution:
    def largestPermutation(self,B,nums):
        if B >= len(nums)//2:
            return sorted(nums,key = lambda x:-x)
        temp = nums.copy()
        for index,num in enumerate(temp):
            temp[index] = (num,index)
        temp.sort()
        for index in range(B):
            if nums[index] != temp[-1][0]:
                max,max_index = temp.pop()
                nums[index],nums[max_index] = nums[max_index],nums[index]
        return nums 
solution = Solution()
B = int(input())
nums = list(map(int,input().split()))
result = solution.largestPermutation(B,nums)       
print(result)