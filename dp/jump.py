from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for index in range(len(nums)):
            if index > end:
                return False
            end = max(end, index + nums[index])
        return True
solution = Solution()
nums=  list(map(int, input().split()))
result = solution.canJump(nums)
print(result)
