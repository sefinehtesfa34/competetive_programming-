
# from typing import List
# class Solution:
#     #Function to detect cycle in an undirected graph.
# 	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
# 		visited = set()
# 		def dfs(v, prev):
# 		    visited.add(v)
#             for child in adj[v]:
#                 if child != prev and child in visited:
#                     return 1
#                 elif child in visited:
#                     continue
#                 if dfs(child, v):
#                     return 1
#             return 0
#         for index in range(V):
#         if index in visited:
#             continue 
#         if dfs(index, index):
#             return 1
#     return 0