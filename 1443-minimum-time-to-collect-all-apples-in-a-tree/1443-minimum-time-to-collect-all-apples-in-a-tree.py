class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for left,right in edges:
            graph[left].append(right)
            graph[right].append(left)
        def dfs(current, parent):
            if current != parent and len(graph[current]) == 1:
                return 2 if hasApple[current] else 0
            ans = 0
            for child in graph[current]:
                if child != parent:
                    ans += dfs(child, current)
            return ans + 2 if (ans == 0 and hasApple[current]) or ans > 0 else ans
        return max(dfs(0, 0) - 2, 0)
    
    
        
        
        