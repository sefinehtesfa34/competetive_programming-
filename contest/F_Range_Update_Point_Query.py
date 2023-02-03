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
        n, q = get_nums()
        nums = get_nums()
        pre = [0]*(n + 2)
        ans = [0]*(n)
        for _ in range(q):
            lf, rt = get_nums()
            pre[lf] += 1
            pre[rt + 1] -= 1
        for index in range(1, n):
            pre[index] += pre[index - 1]
        for index in range(n):
            num = str(nums[index])
            while len(num)
            
        
            
        
main()
