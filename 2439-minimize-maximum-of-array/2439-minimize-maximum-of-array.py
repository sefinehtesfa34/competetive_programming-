class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can_make(value):
            dp = [0]*len(nums)
            dp[-1] = nums[-1]
            for index in range(len(nums) - 2,- 1, -1):
                remain = max(0, dp[index + 1] - value)
                dp[index + 1] -= max(0, remain)
                dp[index] = nums[index] + max(0, remain)
            return max(dp) <= value
        low = 0
        high = max(nums)
        while low < high:
            mid = (low + high)//2
            is_valid = can_make(mid)
            if is_valid:
                high = mid
            else:
                low = mid + 1
        return high
        
        
        
                    
                    
                    
                
    
                