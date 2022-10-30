class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.nodes = set()
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        priority_queue = [(0, k)]
        
        while priority_queue:
            weight, node = heappop(priority_queue)
            self.nodes.add(node)
            if len(self.nodes) == n:
                return weight
            for child, child_weight in graph[node]:
                if child not in self.nodes:
                    heappush(priority_queue, (weight + child_weight, child))
        return -1
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        