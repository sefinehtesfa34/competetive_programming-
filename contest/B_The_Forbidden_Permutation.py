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
        n, m, d = get_nums()
        nums = get_nums()
        a = get_nums()
        hashmap  = {num:index + 1 for index , num in enumerate(nums)}
        left = 0
        right = 1
        ans = n
        while right < m:
            lf = hashmap[a[left]]
            rt = hashmap[a[right]]
            if n - 1 > d:
                ans = min(ans, d - (rt -lf) + 1)
            ans = min(ans, rt-lf)
            right +=1
            left += 1
        print(max(0, ans))
        
main()
