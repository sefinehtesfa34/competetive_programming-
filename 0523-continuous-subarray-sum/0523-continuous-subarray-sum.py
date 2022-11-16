class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo = {0:-1}
        cur_sum = 0
        for index in range(len(nums)):
            cur_sum += nums[index]
            if cur_sum % k in modulo:
                if index - modulo[cur_sum % k] >= 2:
                    return True
            else:
                modulo[cur_sum % k] = index
        
        return False
    # [23,2,4,6,6]
# 7
    