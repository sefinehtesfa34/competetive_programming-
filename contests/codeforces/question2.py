from typing import Counter


t = int(input())
while t:
    # n,k = list(map(int, input().split()))
    n = int(input())
    nums= list(map(int, input().split()))
    counter = Counter(nums)
    duplicate = {}
    move = 0
    for val in counter:
        if counter[val] > 1:
            duplicate[val] = counter[val] - 1
    for num in nums:
        if len(duplicate) == 0:
            break 
        if num in duplicate:
            duplicate[num] -= 1
            if duplicate[num] == 0:
                 del duplicate[num]
        move += 1
    print(move)
    # 1 1 2 1 
    # 1 2 1 7 1 2 1
    # {1:4,2:2,7:1}
    # 4 
    
    
    t-=1 