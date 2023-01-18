class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        prefix = [0]*(len(nums))
        prefix[0] = nums[0]
        dp = [0]*len(nums)
        cur_sum = -inf
        best_sum = -inf
        max_pref = -inf
        for index in range(1, len(nums)):
            prefix[index] = prefix[index - 1] + nums[index]
        for index in range(len(nums)):
            cur_sum = max(nums[index], cur_sum + nums[index])
            best_sum = max(best_sum, cur_sum)
            best_sum = max(best_sum, max_pref + prefix[-1] - prefix[index])
            max_pref = max(max_pref, prefix[index])
        return best_sum
    