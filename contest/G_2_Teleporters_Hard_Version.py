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
        cur = [num + index + 1 for index, num in enumerate(nums)]
        
        min_val = 1000000
        cur_index = 0
        for index in range(n):
            if cur[index] < min_val:
                min_val = cur[index]
                cur_index = index 
        c -= min_val
        nums[cur_index] = 10000000000000
        res = [num + min(index + 1, n - index) for index, num in enumerate(nums)]
        res.sort()        
        count = 1 if c >= 0 else 0 
        index = 0
        cur_sum = 0
        while index < n and cur_sum + res[index] <= c:
            cur_sum += res[index]
            index += 1
            count += 1
        print(count)
            
                
main()
