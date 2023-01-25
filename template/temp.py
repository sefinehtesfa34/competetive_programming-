from math import floor
from itertools import accumulate
from functools import cache
from heapq import *
from collections import *
from math import ceil, log2 
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def yes():
    return print("YES")
def no():
    return print("NO")

def main():
    test = get_int()
    for _ in range(test):
        n,x = get_nums()
        if x > n:
            print(-1)
        elif x == 0:
            bits = bin(n)[2:]
            leng = len(bits) - 1
            index = bits.find('1')
            size = leng - index 
            print(1 << size + 1)
        else:
            diff = n - x 
            keep = diff 
            ans = n 
            if diff % 2 == 1:
                diff -= 1
                ans &= ~(1 << 0)
            if diff & (diff - 1) != 0:
                diff -= 2
                ans &= ~(1 << 1)
            if diff != 0 and (diff & (diff - 1) == 0):
                ans &= ~(1 << int(log2(diff)))
            bit = 0 
            bits = bin(x)[2:]
            leng = len(bits) - 1
            index = bits.find('1')
            leftmost = leng - index  + 1
            end = leftmost
            
            while (x + 2*(2**leftmost) - 1 - keep) >= n:
                end = leftmost
                leftmost -= 1
            cand = []
            for index in range(end + 1):
                if n & 1 << index:
                    continue 
                cand.append(2**index)
            @cache
            def dp(index, sum):
                if sum + x >= n:
                    return sum + x 
                if index == len(cand):
                    return float('inf')
                pick = dp(index + 1, sum + cand[index])
                notPick = dp(index + 1, sum)
                return min(pick, notPick)
            ans = dp(0, 0)
            print(ans)
            
                
            
                
            
            
            
            
        
        # nums = get_nums()
    # print(*output)
    # yes()
    # no()
    
    
main()