def dfs(nums):
    if len(nums) == 1:
        return 1
    
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    