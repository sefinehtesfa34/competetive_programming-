import math
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(range(1, 10))
    answer = []
    def dp(target, index, temp = ''):
        if target == 0:
            return int(temp)
        if index == len(nums) or target < 0:
            return math.inf
        take = dp(target - nums[index], index + 1, temp + str(nums[index]))
        notTake = dp(target, index + 1, temp)
        return min(take, notTake)
    result = dp(n, 0)
    print(result)
        