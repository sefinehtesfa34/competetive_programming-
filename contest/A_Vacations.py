from collections import * 
from heapq import *
from itertools import accumulate,permutations,product,combinations
# print(list(permutations([1, 2, 4 ,5], 3)))
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))

def main():
    n = get_int()
    nums = get_nums()
    dp = [[0, 0, 0] for _ in range(n + 1)]
    max_res = 0
    for index in range(1, n + 1):
        dp[index][0] = max(dp[index - 1])
        if nums[index - 1] == 1 or nums[index - 1] == 3:
            dp[index][1] = 1 + max(dp[index - 1][0], dp[index - 1][2]) 
        if nums[index - 1] == 2 or nums[index - 1] == 3:
            dp[index][2] = 1 + max(dp[index - 1][0], dp[index - 1][1])
        max_res = max(max_res, max(dp[index])) 
    print(n - max_res)
                
                
                
            
        
        
                    
                
main()
