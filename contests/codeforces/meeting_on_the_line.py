from math import ceil


t = int(input())
for _ in range(t):
    n = int(input())
    xi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    left = 1
    right = 10e8
    leftSum = 0
    rightSum = 1
    while left + 10e-6 < right:
        mid = (left + right)/2 
        ceilIndex = ceil(mid)
        leftSum = 0
        rightSum = 0
        for index in range(len(xi)):
            if index <= ceilIndex:
                leftSum = max(leftSum, ti[index] + abs(xi[index] - mid))
            else:
                rightSum = max(rightSum, ti[index] + abs(xi[index] - mid))
        if rightSum > leftSum:
            left = mid + 1
        else:
            right = mid - 1
    print(mid + 1) 
    
 
        
        
        