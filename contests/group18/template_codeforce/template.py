from collections import * 
from heapq import * 
from math import * 
from functools import * 
from bisect import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def get_n_m():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = get_nums()
        nums.sort(reverse = True)
        left = 0
        right = 1
        answer = 0
        while right < len(nums) - 1:
            answer  = max(nums[left] - nums[right] + nums[left] - nums[-1], answer)
            right += 1
            left += 1
        print(answer)
        
        
        
        
main()