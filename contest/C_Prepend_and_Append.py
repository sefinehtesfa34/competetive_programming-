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
        nums = input()
        left = 0
        right = n-1
        count = 0
        while left < right:
            if nums[left] == "1":
                count += 1
            else:
                count -= 1
            if nums[right] == '1':
                count += 1
            else:
                count -= 1
            if count != 0:
                print(right - left + 1)
                break 
            left += 1
            right -= 1
        else:
            print(abs(right - left + 1))
        
        
main()
