from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        
        DIR=[(1,0),(0,1),(-1,0),(0,-1)]
        def isBound(row,col):
            return 0<=row and row<m and 0<=col and col<n
        for row,col in guards:
            grid[row][col]="G"
        for row,col in walls:
            grid[row][col]="W"
        for row,col in guards:
            for position in DIR:
                new_row=row+position[0]
                new_col=col+position[1]
                
                while isBound(new_row,new_col) and \
                    (grid[new_row][new_col]==0 \
                     or grid[new_row][new_col]==1\
                    ):
                    
                    grid[new_row][new_col]=1
                    new_row+=position[0]
                    new_col+=position[1]
                
                    
        counter=0
        for row in grid:
            for index in range(len(row)):
                if row[index]==0:
                    counter+=1
        return counter
        
        
                    
        
        
