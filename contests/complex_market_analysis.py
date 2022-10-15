def findOnes(left, right, index):
    count = 1
    while left >=0 and nums[left] == 1:
        if left + e * index <= n:
            count += index - left
        left -= 1
    while right < len(nums) and nums[right] == 1:
        if index + e * right <= n:
            count += right - left 
        right += 1
    print(left, right)
    return count 
def checkPrime(num):
    index = 2
    while index * index <= num:
        if num % index == 0:
            return False
        index += 1
    return True
t = int(input())
for _ in range(t):
    n, e = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    totalCount = 0
    for index in range(len(nums)):
        if checkPrime(nums[index]):
            totalCount += findOnes(index - 1, index + 1, index)
    print(totalCount)
    