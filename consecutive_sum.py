t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for index in range(k):
        maxVal = nums[index]
        right = -1
        for begin in range(index + 1, len(nums)):
            if index % k == begin % k:
                if nums[begin] > maxVal:
                    right = begin
                    maxVal = nums[begin] 
        if right == -1:
            continue
        nums[right], nums[index] = nums[index], nums[right]
    print(sum(nums[:k]))
    
            # [1 0 7 6 8 3 2]