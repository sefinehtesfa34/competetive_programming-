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
        n = get_int()
        nums = get_nums()
        neg = 0
        for index in range(n):
            neg += 1 if nums[index] < 0 else 0 
        nums = [abs(num) for num in nums]
        sums = sum(nums)
        if neg % 2 == 0:
            print(sums)
        else:
            print(sums - 2*min(nums))
            
        
            
                
        
main()
