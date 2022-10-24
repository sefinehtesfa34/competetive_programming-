from collections import defaultdict


class Solution:
    def reachable(self):
        vertices = int(input())
        start_node = self.get_start_node()
        end_node = self.get_end_node()
        graph = self.get_graph()
        dp = [False]*vertices
        dp[end_node] = True 
        visited = set()
        stack = [end_node]
        
        while stack:
            current_node = stack.pop()
            if current_node == start_node:
                return True 
            visited.add(current_node)
            for neighbor in graph[current_node]:
                dp[neighbor] = dp[neighbor] or dp[current_node]
                if neighbor not in visited:
                    stack.append(neighbor)

        return False 
        
            
        
    def get_start_node(self):
        return int(input())
    
    def get_end_node(self):
        return int(input())
    
    def get_graph(self):
        edges = int(input())
        graph = defaultdict(list)
        
        for _ in range(edges):
            node1, node2 = list(map(int, input().split()))
            graph[node1].append(node2)
            
        
        return graph 
    
solution = Solution()
result = solution.reachable()
print(result)
