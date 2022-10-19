class Solution:
    def build_grid(self, n):
        grid = [['.']*n for _ in range(n)]
        return grid 
    
    def get_grid(self):
        return int(input())
    
    def n_queen(self):
        n = self.get_grid()
        grid = self.build_grid(n)
        columns = [True]*n 
        left_diagonal = [True] * (2*n )
        right_diagonal = [True] * (2*n)
        return self.valid_queens(grid, columns, left_diagonal, right_diagonal, n)
    
    def valid_queens(self, grid,columns,left_diagonal, right_diagonal, n, row = 0):
        if row == n:
            return 
        for col in range(n):
            if columns[col] and right_diagonal[col + row] and left_diagonal[row - col + (n - 1)]:
                grid[row][col] = 'Q'
                columns[col] = True 
                left_diagonal[row + col] = True 
                right_diagonal[row - col + (n - 1)] = True 
                self.valid_queens(grid, columns, left_diagonal, right_diagonal, n, row + 1)
                grid[row][col] = '.'
                columns[col] = False
                left_diagonal[row + col] = False 
                right_diagonal[row - col + (n - 1)] = False 
        return grid 
    
solution = Solution()
result_grid = solution.n_queen()
print(result_grid)
    
    
            
            
        
        
        
        
    