from typing import *
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = y = x = 0
        for index in range(len(nums)):
            xor ^= (index + 1) ^ nums[index]
            
        for index in range(len(nums)):
            if (index + 1) & (xor&-xor):
                x ^= (index + 1)
            else:
                y ^= (index + 1)
            if nums[index] & (xor&-xor):
                x ^= nums[index]
            else:
                y ^= nums[index]
        
        return [x, y]
solution = Solution()
nums = list(map(int, input().split()))
result = solution.findErrorNums(nums)
print(result)
