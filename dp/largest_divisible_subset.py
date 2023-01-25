from math import lcm


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp =[[0, 0] for _ in range(len(nums))]
        cur_index = cur_max = 0
        for index in range(len(nums)):
            dp[index][1] = nums[index]
            dp[index][0] = 1
        for index in range(len(nums)):
            for left in range(index):
                if dp[index][0] <= dp[left][0] and nums[index] % dp[left][1] == 0:
                    dp[index][0] = 1 + dp[left][0]
                    dp[index][1] = lcm(dp[left][1], nums[index]) 
                if dp[index][0] > cur_max:
                    cur_index = index
                    cur_max = dp[index][0]
        answer = []
        while cur_index >= 0:
            answer.append(nums[cur_index])
            shift_pos = cur_index - 1
            if dp[cur_index][0] == 1:
                return answer
            cur_len = 0
            for index in range(cur_index):
                if lcm(dp[index][1], nums[cur_index]) == dp[cur_index][1]:
                    if dp[index][0] > cur_len:
                        cur_len = dp[index][0]
                        shift_pos = index
            cur_index = shift_pos
        return answer
    
    
    
        