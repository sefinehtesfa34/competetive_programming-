
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        answer = []
        for index in range(len(nums)):
            for left in range(index):
                if nums[index] % nums[left] == 0:
                    dp[index] = max(dp[index], 1 + dp[left])
        index = dp.index(max(dp))
        while index >= 0:
            answer.append(nums[index])
            shift_index = index - 1
            max_len = 0
            if dp[index] == 1:
                return answer
            for left in range(index):
                if nums[index] % nums[left] == 0 and dp[left] > max_len:
                    max_len = dp[left]
                    shift_index = left
            index = shift_index
        return answer