from collections import * 
from heapq import *
from itertools import accumulate,permutations,product,combinations
# print(list(permutations([1, 2, 4 ,5], 3)))
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))

def main():
    test = get_int()
    for _ in range(test):
        n, c= get_nums()
        nums = get_nums()
        min_val = float('inf')
        cur_index = -1
        for index in range(n):
            if index + 1 <= n - index and index + 1 + nums[index] < min_val:
                cur_index = index 
                min_val = nums[index] + index + 1
        c-= min_val
        count = 1 if c >= 0 else 0
        nums[cur_index] = float('inf')
        cur = [num + min(index + 1, n - index) for index, num in enumerate(nums)]
        cur.sort()
        cur_sum = 0
        for index in range(n):
            cur_sum += cur[index]
            if cur_sum > c:
                break 
            count += 1
        print(count)
            
            
        
        
                    
                
main()
