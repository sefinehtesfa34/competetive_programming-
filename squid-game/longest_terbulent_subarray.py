# from typing import List


# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         dp = [[0, 0] for _ in range(len(arr) + 1)]
#         nums = []
#         for index in range(1, len(arr)):
#             nums.append(1 if arr[index - 1] - arr[index] > 0 else -1)
#         nums.append(1)
#         print(nums)
#         for index in range(1, len(nums)):
#             if nums[index - 1] < nums[index]:
#                 dp[index][0] = 1 + dp[index - 1][1]
#             else:
#                 dp[index][1] = 1 + dp[index - 1][0]
#         return max([max(values) for values in dp])
# sol = Solution()
# nums = [9,4,2,10,7,8,8,1,9]
# nums = [4,8,12,16]
# print(sol.maxTurbulenceSize(nums))
    
            
        
        