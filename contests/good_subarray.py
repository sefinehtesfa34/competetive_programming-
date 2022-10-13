t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    left = right = numSubarrays = 0
    while right < len(nums):
        if nums[right] < right - left + 1:
            left = right 
        numSubarrays += right - left + 1
        right += 1
    print(numSubarrays)
    