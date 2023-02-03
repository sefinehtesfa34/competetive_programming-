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
        word = input()
        count = Counter(word)
        cur_max = 0
        lt_c = Counter()
        for char in word:
            cur_max = max(cur_max, len(lt_c) + len(count))
            count[char] -= 1
            if count[char] == 0:
                del count[char]
            lt_c[char] += 1
            cur_max = max(cur_max, len(lt_c) + len(count))
        print(cur_max)
        
        
main()
