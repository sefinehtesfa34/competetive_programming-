class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(left, right, turn):
            if left > right:
                return 0
            if turn:
                left_chose = nums[left] + dp(left + 1, right, False)
                right_chose = nums[right] + dp(left, right - 1, False)
                return max(left_chose, right_chose)
            left_chose = -nums[left] + dp(left + 1, right, True)
            right_chose = -nums[right] + dp(left, right - 1, True)
            return min(left_chose, right_chose)
        
        return dp(0, len(nums) - 1, True) >= 0
    
            
            