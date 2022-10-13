t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    left = right = numSubarrays = 0
    while right < len(nums):
        while nums[right] < right - left + 1:
            left += 1
        numSubarrays += right - left + 1
        right += 1
    print(numSubarrays)
    