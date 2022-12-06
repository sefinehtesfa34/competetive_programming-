class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        dp = [[0]*k for _ in range(n)]
        memo = {}
        for fro, to, cost in flights:
            graph[fro].append((to, cost))
        memo = {}
        def dp(src, k):
            if (src, k) in memo:
                return memo[src, k]
            
            if src == dst and k >= -1:
                return 0
            if k <= -1:
                return inf
            min_cost = inf
            for child, cost in graph[src]:
                min_cost = min(min_cost, cost + dp(child, k - 1))
            memo[src, k] =  min_cost
            return min_cost
        result = dp(src, k)
        return result if result != inf else -1
            
            
        