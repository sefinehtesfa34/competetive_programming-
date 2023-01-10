from collections import * 
from heapq import *
# from functools import cache
from itertools import accumulate as acu
hpush = heappush
hpop = heappop 

def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))

def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        if n == 2:
            print('YES')
            print(1, 2)
        else:
            print('NO')
main()