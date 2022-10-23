class Solution:
    def target_sum(self):
        
        target = self.get_target()
        nums = self.get_nums()
        dp = [[False]*(len(nums) + 1) for _ in range(target + 1)]
        for index in range(len(nums) + 1):
            dp[0][index] = True 
            
        for current_target in range(1, target + 1):
            for each_index in range(1, len(nums) + 1):
                if nums[each_index - 1] <= current_target:
                    dp[current_target][each_index] = dp[current_target - nums[each_index - 1]][each_index - 1] \
                                            or dp[current_target][each_index - 1]
                
                    
        print(dp)
        print(dp[target][len(nums)])
        
    #     return print(self.dp(0, nums, target))
    
    # def dp(self, index, nums, target_sum):
    #     if target_sum == 0:
    #         return True 
    #     if target_sum < 0 or index == len(nums):
    #         return False 
    #     take = self.dp(index + 1, nums, target_sum - nums[index])
    #     not_take = self.dp(index + 1, nums, target_sum)
    #     return take or not_take 
    '''
    '''
    
        
    def get_target(self):
        return int(input())
    
    def get_nums(self):
        return list(map(int, input().split()))
    
solution = Solution()
solution.target_sum()

        