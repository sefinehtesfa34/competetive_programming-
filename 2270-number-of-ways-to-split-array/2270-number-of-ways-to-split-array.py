class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        count = cur_sum = 0
        for num in nums[:-1]:
            cur_sum += num
            if cur_sum >= total_sum - cur_sum:
                count += 1
        return count
    