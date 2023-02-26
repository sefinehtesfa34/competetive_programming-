from collections import *
import sys
import threading
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    graph = defaultdict(list)
    count = [0]*(n + 1)
    dp = [0]*(n + 1)
    ans = 0
    for _ in range(n - 1):
        a, b = get_nums()
        graph[a].append(b)
        graph[b].append(a)
    def dfs1(root, parent):
        count[root] = 1
        for child in graph[root]:
            if child != parent:
                dfs1(child, root)
                count[root] += count[child]
                dp[root] += dp[child]
        dp[root] += count[root]
    def dfs2(root, parent):
        nonlocal ans 
        for child in graph[root]:
            if child != parent:
                root_value = dp[root] - count[child] - dp[child]
                cur_value = dp[child] + n - count[child]
                dp[child] = max(dp[child], root_value  + cur_value)
                dfs2(child, root)
    dfs1(1, -1)
    dfs2(1, -1)
    print(max(dp))
    
threading.stack_size(1<<27)
sys.setrecursionlimit(1<<30)
 
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()