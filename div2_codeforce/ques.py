from itertools import accumulate


n, m = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
prefix = list(accumulate(nums1, initial=0))
answer = []
start = ramining = 0
for num in nums2:
    left = start + 1
    right = len(nums1) - 1
    while left <= right:
        mid = (left + right) // 2
        if ramining + prefix[mid] - prefix[start] <= num:
            left = mid + 1
        else:
            right = mid - 1 
    remaining = max(0, prefix[left] - prefix[start] - num)
    start = right if left < n else 0
    answer = n - right if left < n else n 
    print(answer)
    
        
     
    
        
    
