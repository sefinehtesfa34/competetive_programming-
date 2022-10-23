class Solution:
    def robot_moves(self):
        n, m = list(map(int, input().split()))
        grid = self.get_grid(n, m)
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        dp[n - 1][m - 1] = 1
        for row in range(n - 1,-1, -1):
            for col in range(m - 1, -1, -1):
                if grid[row][col] != -1:
                    dp[row][col] += dp[row][col + 1] + dp[row + 1][col]
        return print(dp[0][0])
        
    def get_grid(self, n, m):
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        return grid 
solution = Solution()
solution.robot_moves()
    