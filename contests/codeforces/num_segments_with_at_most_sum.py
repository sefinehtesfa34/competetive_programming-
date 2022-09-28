n, s  = list(map(int, input().split()))
nums = list(map(int, input().split()))
answer = 0
left = 0
right = 0
sum = 0
while  right < len(nums):
    sum += nums[right]
    while sum > s and left < len(nums):
        sum -= nums[left]
        left += 1
    answer += (right - left + 1)
    right += 1
print(answer)

