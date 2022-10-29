from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        '''
        
        [1]
        
        [2,1]
        
        '''
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp)
    
        
        
        
        
        
                
                