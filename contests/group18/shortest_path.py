from math import *
from heapq import *
from typing import *

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        distance = {node:inf for node in range(1, n + 1)}
        graph, weights = self.get_graph(edges, n)     
        distance[n] = 0
        heap = [(0, n)]
        visited = set()
        
        # find the shortest distance from n to all of the given node using dijkstra's algo.
        while heap:
            weight, node = heappop(heap)
            visited.add(node)
            for child in graph[node]:
                if child not in visited and weight + weights[node][child] < distance[child]:
                    distance[child] = weight + weights[node][child]
                    heappush(heap, (distance[child], child))
        result = self.dfs(graph, n,  1, distance, {}, set())
        return result % (10 ** 9 + 7)
    
    # Using graph traversal, count the possible paths
    def dfs(self, graph, n, current, distance, memo, visited):
        if current in memo:
            return memo[current]
        if current == n: 
            return 1
        counter = 0
        visited.add(current)
        for child in graph[current]:
            if child not in visited and distance[child] < distance[current]:
                counter += self.dfs(graph, n, child, distance, memo, visited)
        visited.remove(current)    
        memo[current] =  counter
        return memo[current]
    
    def get_graph(self, edges, n):
        graph = {node:[] for node in range(1, n + 1)}
        weights = [[0]*(n  + 1) for _ in range(n + 1)]
        for left, right, weight in edges:
            graph[left].append(right)
            graph[right].append(left)
            weights[left][right] = weight
            weights[right][left] = weight
        return graph, weights
solution = Solution()
n = 15
edges = [[1, 2, 3],[1, 3, 3], [2, 3, 2], [2,4,3], [3,4,2], [4,2,1],[1,3,1],[1,4,1],[1,5,1],[5,6,1],[6,7,1],[7,8,1],[8,9,1],[9,10,1],[10,11,1],[11,12,1],[12,13,1],[13,14,1],[14,15,1]]
result = solution.countRestrictedPaths(n, edges)
print(result)      
        
'''
 [[1, 2, 3],[1, 3, 3], [2, 3, 2], [2,4,3], [3,4,2]]

'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        