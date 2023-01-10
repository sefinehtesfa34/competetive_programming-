class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target_sum =  total_sum // 2
        dp = [[0]*(target_sum + 1) for _ in range(len(nums) + 1)]
        for row in range(1, len(nums) + 1):
            dp[row][0] = True
            for target in range(1, target_sum + 1):
                if target >= nums[row - 1]:
                    dp[row][target] = dp[row - 1][target - nums[row - 1]] or dp[row - 1][target]
                else:
                    dp[row][target] = dp[row - 1][target]
        return dp[len(nums)][target_sum]
    