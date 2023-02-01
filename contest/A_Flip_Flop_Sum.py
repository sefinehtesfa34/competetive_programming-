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
        count = 0
        neg = -4
        for index in range(1, n):
            if nums[index - 1] == nums[index] == -1:
                count = 4
            if nums[index] == -1 or nums[index - 1] == -1:
                neg = 0 
        print(sum(nums) + count + neg)
        
        
main()
