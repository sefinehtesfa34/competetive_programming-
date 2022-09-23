t = int(input())
while t:
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    oper = max(nums)
    left = 0
    right = 2
    while right < len(nums):
        diff = nums[left + 1] - nums[left] + nums[right] - nums[left + 1]
        oper = min(oper, diff)
        left += 1
        right += 1
    print(oper)
    t-=1 
