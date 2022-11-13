class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = {}
        self.longest = -2
        done = set()
        for node in range(len(edges)):
            if edges[node] != -1:
                graph[node] = edges[node]
        distance = Counter()
        def dfs(current, distance, visited):
            if current in done:
                return 
            
            if current not in graph:
                return 
            visited.add(current) 
            done.add(current)
            child = graph[current]
            if child in visited:
                self.longest = max(self.longest, abs(distance[current] - distance[child]))
                return
            distance[child] = distance[current] + 1
            dfs(child, distance, visited)
        for node in range(len(edges)):
            if node not in done:
                dfs(node, Counter(), set())
        return self.longest + 1
    