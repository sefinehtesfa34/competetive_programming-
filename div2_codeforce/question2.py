

from math import gcd, lcm


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if len(nums) <= 2:
        print("YES")
    else:
        for index in range(len(nums) - 1):
            if gcd(nums[index], lcm(nums[index], nums[index + 1])) != nums[index + 1]:
                print("NO")
                break 
        else:
            print("YES")
            
    
        
        
        
    