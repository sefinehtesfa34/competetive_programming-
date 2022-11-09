class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        distance = {node:inf for node in range(1, n + 1)}
        graph = self.get_graph(edges, n)     
        distance[n] = 0
        heap = [(0, n)]
        visited = set()
        
        # find the shortest distance from n to all of the given node using dijkstra's algo.
        while heap:
            cur_weight, node = heappop(heap)
            visited.add(node)
            for weight, child in graph[node]:
                if child not in visited and weight + cur_weight < distance[child]:
                    distance[child] = cur_weight + weight
                    heappush(heap, (distance[child], child))
                
        return self.dfs(graph, n,  1, distance, {}, set()) % (10 ** 9 + 7)
    
    # Using graph traversal, count the possible paths
    def dfs(self, graph, n, current, distance, memo, visited):
        if current in memo:
            return memo[current]
        if current == n: 
            return 1
        counter = 0
        visited.add(current)
        for _, child in graph[current]:
            if child not in visited and distance[child] < distance[current]:
                counter = (counter + self.dfs(graph, n, child, distance, memo, visited)) % (10**9 + 7)
        visited.remove(current)    
        memo[current] =  counter
        return memo[current]
    
    def get_graph(self, edges, n):
        graph = {node:[] for node in range(1, n + 1)}
        for left, right, weight in edges:
            graph[left].append((weight, right))
            graph[right].append((weight, left))
            
        return graph
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        