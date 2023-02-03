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
        n, c= get_nums()
        nums = get_nums()
        heap = [num + index + 1 for index, num in enumerate(nums)]
        heapify(heap)
        count = 0
        while heap and  c >= heap[0]:
            c -= heappop(heap)
            count += 1
        print(count)
            
        
        
            
                
        
main()
