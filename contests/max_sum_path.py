class Solution:
    def max_sum_path(self):
        n, m = self.get_row_col()
        grid = self.get_grid(n, m)
        # create a 2D array to compute the possible path sum
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        
        # start from the bottom up and calculate the maximum sum along the path
        for row in range(n, 0, -1):
            for col in range(m, 0, -1):
                dp[row - 1][col - 1] = grid[row - 1][col - 1] + max(dp[row - 1][col], dp[row][col - 1])
        
        return print(dp[0][0])
        
        
        
    def get_grid(self, n, m):
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        return grid 
    
    def get_row_col(self):
        return list(map(int, input().split()))
solution = Solution()
solution.max_sum_path()
