# from collections import *
# import sys
# import threading
# def get_int():
#     return int(input())
# def get_nums():
#     return list(map(int, input().split()))
# def main():
#     n, Mod = get_nums()
#     graph = defaultdict(list)
#     dp1 = [0]*(n + 1)
#     dp2 = [1]*(n + 1)
#     for _ in range(n - 1):
#         a, b = get_nums()
#         graph[a].append(b)
#         graph[b].append(a)
#     def dfs(root, parent):
#         dp1[root] = 1
#         for child in graph[root]:
#             if child != parent:
#                 dfs(child, root)
#                 dp1[root] *= (1 + dp1[child])
#     def dfs2(root, parent):
#         for child in graph[root]:
#             if child != parent:
#                 dp2[child] *= dp2[root]
#                 dp2[child] += 1  
#                 dfs2(child, root)
#     dfs(1, -1)
#     dfs2(1, -1)
#     print(dp1)
#     print(dp2)
# threading.stack_size(1<<27)
# sys.setrecursionlimit(1<<30)
 
# main_thread = threading.Thread(target = main)
# main_thread.start()
# main_thread.join()