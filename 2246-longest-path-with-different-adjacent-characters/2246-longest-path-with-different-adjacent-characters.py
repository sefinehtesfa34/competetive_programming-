class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        self.max = 0
        for node in range(len(parent)):
            graph[parent[node]].append(node)
        def dfs(current, par):
            first_max = second_max = 0
            for child in graph[current]:
                if child == par:
                    continue
                cur_max = dfs(child, current)
                if s[child] != s[current]:
                    second_max = max(second_max, min(first_max, cur_max))
                    first_max = max(first_max, cur_max)
            self.max = max(self.max, 1 + first_max + second_max)
            return 1 + first_max
        dfs(0, -1)
        return self.max
        
        
        
            