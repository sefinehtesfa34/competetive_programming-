class Solution:
    def maximalRectangle(self, matrix):
        n, m = len(matrix), len(matrix[0])
        heights = [0]*m
        max_area = 0
        for row in range(n):
            for col in range(m):
                heights[col] = (heights[col] + 1) if matrix[row][col] == '1' else 0
            stack = []
            for index in range(len(heights) + 1):
                while stack and (index == len(heights) or heights[stack[-1]] > heights[index]):
                    width = heights[stack.pop()]
                    length = (index - 1) - (stack[-1] if stack else -1)
                    max_area = max(max_area, width * length)
                stack.append(index)
        return max_area
    
    
                
        
        
        
        
        
        