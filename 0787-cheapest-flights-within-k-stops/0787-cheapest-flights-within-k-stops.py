class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman ford algorigthm
        dp = [inf]*n
        dp[src] = 0
        for _ in range(k + 1):
            temp_dp = dp.copy()
            for fro, to, cost in flights:
                if dp[fro] + cost < temp_dp[to]:
                    temp_dp[to] = cost + dp[fro]
            dp = temp_dp
            
        return dp[dst] if dp[dst] != inf else -1
    
            