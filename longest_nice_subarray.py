from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        xor = left = longest = 0
        for index in range(len(nums)):
            while xor & nums[index]:
                xor ^=  nums[left]
                left += 1
            xor ^= nums[index]
            longest = max(longest, index - left + 1)
        return longest
    
            