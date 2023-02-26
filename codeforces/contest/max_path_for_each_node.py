from collections import defaultdict
import sys
import threading

def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    dp1 = [0]*(n + 1)
    dp2 = [0]*(n + 1) 
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = get_nums()
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs1(root, parent):
        for child in graph[root]:
            if child != parent:
                dp1[child] = 1 + dp1[root]
                dfs1(child, root)
    def dfs2(root, parent):
        for child in graph[root]:
            if child != parent:
                dp2[child] = 1 + dp2[root]
                dfs2(child, root)
    
                       
    dfs1(1, -1)
    left_end = dp1.index(max(dp1))
    dfs2(left_end, -1)
    right_end = dp2.index(max(dp2))
    dp1 = [0]*(n + 1)
    dfs1(right_end, -1)
    ans = [0]*(n)
    for node in range(1, n + 1):
        ans[node - 1] = max(dp1[node], dp2[node])
    print(*ans)
threading.stack_size(1<<27)
sys.setrecursionlimit(1<<30)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()
