from  heapq import * 
from collections import * 
from math import * 

def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n  = input()
        left = 0
        right = 1
        hashmap = Counter()
        answer = 0
        for num in num:
            hashmap[num] += 1
            while hashmap[num] > len(hashmap):
                left += 1
                hashmap[n[left]] -= 1
            answer += 1 
        print(answer)
        
        '''
        welmcoe
        whato me
        '''
        
main()