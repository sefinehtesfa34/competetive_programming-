class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for left, right, weight in roads:
            graph[left].append((weight, right))
            graph[right].append((weight, left))
        ways = [0]*n
        ways[0] = 1
        dist = [inf] * n
        mod = 1000_000_007
        min_heap = [(0, 0)]
        while min_heap:
            weight, node = heappop(min_heap)
            if weight > dist[node]:
                continue 
            for child_weight, child in graph[node]:
                if child_weight + weight < dist[child]:
                    dist[child] = child_weight + weight
                    heappush(min_heap, (dist[child], child))
                    ways[child] = ways[node]
                elif child_weight + weight == dist[child]:
                    ways[child] += ways[node]
        return ways[n - 1] % mod
    
    
    
    
    
    
    
    
    
    
    
    
    
    