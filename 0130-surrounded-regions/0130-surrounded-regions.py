class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        unsurrounded = set()
        visited = set()
        def is_bound(row, col):
            return 0 <= row < n and  0<= col < m
        
        def dfs(row, col, visited):
            unsurrounded.add((row, col))
            visited.add((row, col))
            for row_increase, col_increase in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = row + row_increase
                new_col = col + col_increase
                if is_bound(new_row, new_col) and (new_row, new_col) not in visited:
                    if board[new_row][new_col] == "O":
                        dfs(new_row, new_col ,visited)
        for col in range(m):
            if (0, col) not in visited and board[0][col] == "O":
                dfs(0, col, visited)
            if (n - 1, col) not in visited and board[n - 1][col] == "O":
                dfs(n - 1, col, visited)
        for row in range(n):
            if (row, 0) not in visited and board[row][0] == "O":
                dfs(row, 0, visited)
            if (row, m - 1) not in visited and board[row][m - 1] == "O":
                dfs(row, m - 1, visited)
        for row in range(n):
            for col in range(m):
                if (row, col) not in unsurrounded:
                    board[row][col] = "X"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                                        