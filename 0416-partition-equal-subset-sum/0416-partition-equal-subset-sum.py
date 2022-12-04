class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target_sum =  total_sum // 2
        @cache
        def dp(index, cur_sum):
            if cur_sum == 0:
                return True
            if cur_sum < 0 or index == len(nums):
                return False
            return dp(index + 1, cur_sum - nums[index]) or dp(index + 1, cur_sum)
        return dp(0, target_sum)
    