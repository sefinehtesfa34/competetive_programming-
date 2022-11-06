from heapq import *

def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def search(nums):
    left = 0
    right = max(nums)
    while left <= right:
        mid = (left + right) // 2
        result = check(mid)
        if result:
            left = mid + 1
        else:
            right = mid - 1
    return mid 
def check(nums, k):
    heap = nums.copy()
    heapify(heap)
    while heap:
        
    
        
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = get_nums()
         

main()