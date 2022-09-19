class Solution:
    def __init__(self,nums, target):
        self.nums = nums  
        self.target = target 
    def binarySearch(self,compare,left = 0, right = 0):
        while left <= right:
            mid = (left + right)//2
            if self.nums[mid] == self.target:
                return mid,mid 
            if self.nums[mid] < compare:
                right = mid - 1
            else:
                left = mid + 1
        if self.target >= compare:
            right = left - 1
            left = 0
        return left, right 
    def search(self):
         left, right = self.binarySearch(self.nums[0],0, len(self.nums) - 1)
         low, high = self.binarySearch(num,left, right)
         return low if low == high else -1
num = int(input())
nums = list(map(int,input().split()))
solution = Solution(nums,num)
result = solution.search()
print(result)
