from cmath import inf
from collections import *
from functools import cache
def solve (N, A, K):
    partition = {}
    def find_max(partition):
        profit = 0 
        for part in partition:
            if part % 2 == 0:
                profit -= partition[part]
            else:
                profit += partition[part]
        return profit 
    
    def dp(index, start):
        if index == N:
            if len(partition) < K:
                return -inf
            result = find_max(partition)
            return result
        
        max_profit = 0
        for curr in range(start, K):
            if curr not in partition:
                partition[curr] = 0
            partition[curr] += A[index]
            max_profit = max(max_profit, dp(index + 1, curr))
            partition[curr] -= A[index]
            
            if partition[curr] == 0:
                del partition[curr]
        return max_profit
    return dp(0, 0)
    # return result
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = solve(N, A, K)
    print (out_)
