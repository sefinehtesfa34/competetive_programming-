class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        answer = defaultdict(set)
        result = [0]*n
        for parent, child in edges:
            graph[child].add(parent)
            
        def dfs(current, node, visited):
            
            visited.add(current)
            for child in graph[current]:
                if child in visited:
                    continue
                answer[node].add(child)
                dfs(child, node, visited)
                
        for node in range(n):
            dfs(node, node, set())
            
        for index in range(n):
            result[index] = sorted(answer[index])
            
        return result
    
        
            