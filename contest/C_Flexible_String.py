from collections import * 
from heapq import *
from itertools import accumulate,permutations,product,combinations
# print(list(permutations([1, 2, 4 ,5], 3)))
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def solve(n, k, a, b):
    if len(set(a)) <= k:
        return print(n*(n + 1)//2)
    combins = list(combinations(set(a), k))
    max_res = 0
    for comb in combins:
        cur_max = 0
        left = 0
        right = 0
        while right < n:
            if a[right] != b[right] and a[right] not in comb:
                cur_max += (right - left)*(right - left + 1)//2
                left = right + 1
            right += 1
        cur_max += (right - left)*(right - left + 1)//2
        max_res = max(max_res, cur_max)
    return print(max_res)
 
def main():
    test = get_int()
    for _ in range(test):
        n, k = get_nums()
        a = input()
        b = input()
        solve(n, k, a, b)
main()
