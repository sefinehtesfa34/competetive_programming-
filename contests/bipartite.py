from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1]*(len(graph))
        visited = set()
        for node in range(len(graph)):
            colors[node] = 0
            if node not in  visited:
                result = self.dfs(node, graph, colors, visited)
                if not result:
                    return False
        return True 
    
    def dfs(self, current, graph, colors, visited):     
        visited.add(current)
        for neighbor in graph[current]:
            if colors[neighbor] == colors[current]:
                return False 
            colors[neighbor] = int(not colors[current])
            if neighbor not in visited:
                result = self.dfs(neighbor, graph, colors, visited)
                if result == False :
                    return False 
        return True 