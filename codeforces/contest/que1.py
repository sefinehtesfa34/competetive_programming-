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
    n, m = get_nums()
    graph = defaultdict(list)
    for _ in range(m):
        a, b = get_nums()
        graph[a].append(b)
        graph[b].append(a)
    longest = 0
    def dfs(cur_node):
        nonlocal longest
        visited.add(cur_node)
        first_max = second_max = 0
        for left in graph[cur_node]:
            if left in visited:
                continue
            longest_child = 1 + dfs(left)
            second_max = max(second_max, min(first_max, longest_child))
            first_max = max(first_max, longest_child)
        longest = max(longest, first_max + second_max)
        return max(first_max, second_max)
    visited = set()
    dfs(1)
    print(longest)
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
import sys
import threading
sys.setrecursionlimit(1<<30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
# main()
