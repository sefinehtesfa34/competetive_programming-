class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0]*m for _ in range(n)]
        dp[n-1][m-1] = min(0, dungeon[n-1][m-1])
        min_value = 0
        for col in range(m - 2, -1, -1):
            dp[n-1][col] = min(0, dungeon[n-1][col] + dp[n-1][col + 1])
            
        for row in range(n - 2, -1, -1):
            dp[row][m-1] = min(0, dungeon[row][-1] + dp[row + 1][m-1])
        
        for row in range(n - 2, -1, -1):
            for col in range(m - 2, -1, -1):
                dp[row][col] = min(0, dungeon[row][col] + max(dp[row + 1][col], dp[row][col + 1]))
                # min_value = min(min_value, dp[row][col])
                
        return abs(dp[0][0]) + 1
    
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    