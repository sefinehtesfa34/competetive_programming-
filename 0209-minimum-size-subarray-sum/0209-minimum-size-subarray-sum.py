class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 1000_000
        cur_sum = left = 0
        for index in range(len(nums)):
            cur_sum += nums[index]
            while cur_sum >= target:
                cur_sum -= nums[left]
                min_length = min(min_length, index - left + 1)
                left += 1
        return min_length if min_length <= len(nums) else 0
                