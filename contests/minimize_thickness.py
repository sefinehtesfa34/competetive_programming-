t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    total_sum = sum(nums)
    minThickness = n 
    for index in range(1, n + 1):
        curSum = 0
        right = segment = left = 0
        target = total_sum // index
        if target * index != total_sum :
            continue
        curThickness = 0
        while right < n:
            curSum += nums[right]
            if curSum > target:
                break 
            elif curSum == target:
                curThickness = max(curThickness, right - left + 1)
                segment += 1
                left = right + 1
                curSum = 0
            right += 1
        if segment == index:
            minThickness = min(minThickness, curThickness)
    print(minThickness)
    
        
        