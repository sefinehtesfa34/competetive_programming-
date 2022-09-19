class Solution:
    def isSorted(self,nums):
        start = nums[0]
        for num in nums:
            if num < start:
                return False
            start = num 
        return True
        
    def quickSort(self,nums):
        if len(nums) <= 1:
            return nums 
        if self.isSorted(nums):
            return nums 
        mid = len(nums)//2
        left = []
        right = []
        for index, num in enumerate(nums): 
            if mid == index: #one time task
                continue
            if num <= nums[mid]:
                left.append(num)
            else:
                right.append(num)
        return self.quickSort(left) + [nums[mid]] + self.quickSort(right)
            
solution = Solution()
nums = list(map(int,input().split()))
result = solution.quickSort(nums)
print(result)        
