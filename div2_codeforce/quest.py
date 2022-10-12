from collections import defaultdict
from heapq import heappop, heappush
import sys, threading
def main():
    n, k = list(map(int, input().split()))
    values = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(k):
        fr1, fr2 = list(map(int, input().split()))
        graph[fr1].append(fr2)
        graph[fr2].append(fr1)
        
    visited = set()
    total = 0
    golds = []
    for index in range(1, len(values) + 1):
        heappush(golds, (values[index - 1], index))
    def dfs(root):
        if root in visited:
            return 
        visited.add(root)
        for child in graph[root]:
            dfs(child)
    while golds:
        top, index = heappop(golds)
        if index not in visited:
            total += top 
            dfs(index)
    print(total)

    

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()