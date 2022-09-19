# Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted 
# elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest 
# such sequence). 
# EXAMPLE 
# lnput:1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19 
# Output: (3, 9)
from cmath import inf
class Solution:
    def subSort(self,nums):
        n = len(nums)
        leftIndex = 0
        rightIndex = 0 
        leftNum = nums[0]
        rightNum = nums[-1]
        minNum = inf
        maxNum = -inf 
        for index in range(n):
            if nums[index] < leftNum:
                minNum = min(minNum, nums[index])
            else:
                leftNum = nums[index] 
            if rightNum < nums[n - 1 - index]:
                maxNum = max(maxNum, nums[n - 1 - index])
            else:
                rightNum = nums[n - 1 - index]
        for index in range(n):
            if nums[index] > minNum and leftIndex == 0 :
                leftIndex = index 
            if nums[n - index - 1] < maxNum and rightIndex == 0:
                rightIndex = n - index - 1
        return (leftIndex, rightIndex)
          
solution = Solution()
nums = list(map(int,input().split()))
result = solution.subSort(nums)
print(result)
