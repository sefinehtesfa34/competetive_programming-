from collections import defaultdict


class Solution:
    def bipartite(self):
        vertices = int(input())
        edges = int(input())
        graph = self.build_graph(edges)
        colors = [-1]* vertices # Uncolored all vertices initially
        colors[0] = 1 # 1 is a color representation for color Red and 0 is for Blue color. 
        return print(self.dfs(1, graph, colors))
    
    def dfs(self, current, graph, colors, visited = set()):     
        visited.add(current)
        for neighbor in graph[current]:
            if colors[neighbor - 1] == colors[current - 1]:
                return False 
            colors[neighbor - 1] = int(not colors[current - 1])
            if neighbor not in visited:
                result = self.dfs(neighbor, graph, colors, visited)
                if result == False :
                    return False 
        return True 
    
    def build_graph(self,  edges):
        graph = defaultdict(list)
        for _ in range(edges):
            node1, node2 = list(map(int, input().split()))
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph 
        
    
solution = Solution()            
solution.bipartite()
      
        
        