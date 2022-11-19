from math import * 
from functools import *
class Solution:
    def min_abs_diff(self):
        nums = list(map(int, input().split()))
        self.min_diff = inf 
        total_sum = sum(nums)
        # @cache 
        # def dp(index, cur_sum):
        #     self.min_diff = min(self.min_diff, abs(total_sum - 2 * cur_sum))
        #     if index == len(nums):
        #         return 
            
        #     dp(index + 1, cur_sum + nums[index])
        #     dp(index + 1, cur_sum)
            
        # dp(0, 0)
        # return self.min_diff
        dp = [[0]*total_sum for _ in range(len(nums) + 1)]
        dp[]
        for cur_sum in range(1, total_sum):
            

solution = Solution()
result = solution.min_abs_diff()
print(result)
