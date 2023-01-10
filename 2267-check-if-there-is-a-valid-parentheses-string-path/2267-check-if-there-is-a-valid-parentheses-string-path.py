class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        @cache
        def dp(row, col, opened):
            if row == n or col == m or opened < 0:
                return False
            if row == n - 1 and col == m - 1:
                opened += -int(grid[row][col] == ')') + int(grid[row][col] == '(')
                return opened == 0
            opened += 1 if grid[row][col] == '(' else -1
            return dp(row + 1, col, opened) or dp(row, col + 1, opened)
        return dp(0, 0, 0)
    