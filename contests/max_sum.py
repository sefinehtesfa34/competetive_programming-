class Solution:
    def max_sum(self):
        nums = self.get_nums()
        dp = [0]*(len(nums) + 1)
        max_sum = 0
        for index in range(1, len(nums) + 1):
            dp[index] = max(dp[index], nums[index - 1] + dp[index - 1])
            max_sum = max(max_sum, dp[index])
        return print(max_sum)
    def get_nums(self):
        return list(map(int, input().split()))
solution = Solution()
solution.max_sum()

