class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for id in range(n):
            graph[manager[id]].append(id)
        
        def dfs(graph, current_head):
            max_time = 0
            for child in graph[current_head]:
                max_time = max(max_time, informTime[current_head] + dfs(graph, child))
            return max_time
        return dfs(graph, headID)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        