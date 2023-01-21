class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums) + 1)]
        for index in range(len(nums)):
            dp[index][0] = 1
            dp[index][1] = 1
        max_result = 1
        for right in range(1, len(nums)):
            for left in range(right): 
                if nums[right] > nums[left]:
                    dp[right][1] = max(dp[right][1], 1 + dp[left][0])
                    
                elif nums[right] < nums[left]:
                    dp[right][0] = max(dp[right][0], 1 + dp[left][1])
                
                dp[right][1] = max(dp[right][1], dp[left][1])
                dp[right][0] = max(dp[right][0], dp[left][0])
                max_result = max(max_result, dp[right][0], dp[right][1])
        return max_result