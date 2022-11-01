class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # if n == 1 then return 0
        # no price is needed
        
    
        def build_graph(flights):
            graph = defaultdict(list)
            for start, end, price in flights:
                graph[start].append((end, price))
            return graph

        def dfs(graph, sr, dst, k, memo = {}):
            if (sr, k) in memo:
                return memo[(sr, k)]
            # if k is greater than or equal to zero and sr == dst, return the current minimum    
            if sr == dst and k >= -1:
                return 0
            # if sr != dst and k <= 0, this is not a valid path
            if k < 0:
                return inf

            #Find the minimum valid price
            min_path = inf
            for child in graph[sr]:
                min_path = min(min_path, child[1] + dfs(graph, child[0], dst, k - 1))    

            # add the current minimum into the cache
            memo[(sr, k)] = min_path
            return memo[(sr, k)]

        # Build a graph
        graph = build_graph(flights)  
        #traverse the graph
        result = dfs(graph, src, dst, k)
        return result if result != inf else -1
    
        
        
        
        
        
        
        