class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums) + 1)]
        longest = 0
        if not 0 in nums:
            return len(nums) - 1
        #dp[0] = with skip
        #dp[1] = withough skip
        for index in range(len(nums)):
            if nums[index] == 0:
                dp[index][0] = dp[index - 1][1]
            else:
                dp[index][1] = 1 + dp[index - 1][1]
                dp[index][0] = 1 + dp[index - 1][0]
            longest = max(longest, dp[index][0], dp[index][1])
        return longest
    
    
            