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
        n = get_nums()
        word = input()
        up = r = 0
        for char in word:
            if char == 'U':
                up += 1
            if char =='R':
                r += 1
            if char =='L':
                r-=1
            if char =='D':
                up-= 1
            if [up, r] == [1, 1]:
                print("YES")
                break 
        else:
            print("NO")
        
        
main()
