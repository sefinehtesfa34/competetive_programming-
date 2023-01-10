class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0, 0, 0] for _ in range(len(nums) + 1)]
        max_sum = 0
        for index in range(1, len(nums) + 1):
            for mod in range(3):
                cur_sum = dp[index - 1][mod] + nums[index - 1]
                dp[index][cur_sum % 3] = max(dp[index][cur_sum % 3], cur_sum)
                dp[index][mod] = max(dp[index][mod], dp[index - 1][mod])
                
                value = dp[index][cur_sum % 3]
                if value % 3 == 0 and value > max_sum:
                    max_sum = value
        return max_sum
    
    
                    
                