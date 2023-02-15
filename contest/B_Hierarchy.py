from collections import * 
from heapq import *
from itertools import accumulate,permutations,product,combinations
# print(list(permutations([1, 2, 4 ,5], 3)))
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))

def main():
    n = get_int()
    nums = get_nums()
    m = get_int()
    graph = defaultdict(list)
    answer = 0
    for _ in range(m):
        a, b, c = get_nums()
        graph[b].append((a, c))
    count = 0
    nodes = {}
    for node in graph:
        min_cost = float('inf')
        for parent, c in graph[node]:
            if parent in nodes and  nodes[parent] != c:
                count = 1
            if nums[parent - 1] > nums[node - 1]:
                min_cost = min(min_cost, c)
            nodes[parent] = c 
        if min_cost == float('inf') :
            count = 1
        answer += min_cost
    else:
        if count == 1:
            print(-1)
        else:
            print(answer)     
main()
