class Solution:
    def robot(self,grid):
        '''
        O O O O O X
        O O O O O X
        O X O O O O
        O O O O X O
        
        O O O X
        X O O X
        O O O O
        '''
        n = len(grid)
        m = len(grid[0])
        grid[n - 1][m - 1] = 1
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if grid[row][col] != "O":
                    if grid[row][col] =="X":
                        grid[row][col] = 0
                    continue
                grid[row][col] = 0
                if row + 1 < len(grid):
                    grid[row][col] += grid[row + 1][col] 
                if col + 1 < len(grid[0]):
                    grid[row][col] += grid[row][col + 1]
        return grid[0][0]
        
        
        
        
solution = Solution()
row = int(input())
col = int(input())
grid = []
for index in range(row):
    cells = input().split()
    grid.append(cells)
result = solution.robot(grid)
print(result)

