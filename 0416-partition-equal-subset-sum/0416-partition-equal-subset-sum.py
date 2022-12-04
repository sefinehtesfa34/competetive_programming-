class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        target_sum =  total_sum // 2
        if 2*target_sum != total_sum:
            return False
        dp = [False]*(target_sum + 1)
        dp[0] = True
        for index in range(len(nums)):
            visited = set()
            for target in range(1, target_sum + 1):
                if not dp[target] and nums[index] <= target:
                    if target - nums[index] in visited:
                        continue
                    dp[target] = dp[target - nums[index]]
                    visited.add(target)
        return dp[target_sum]
    
    