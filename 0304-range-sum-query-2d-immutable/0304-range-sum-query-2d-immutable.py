class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefixSum=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.prefixSum[row+1][col+1]=matrix[row][col]\
                                             + self.prefixSum[row][col+1]\
                                             + self.prefixSum[row+1][col]\
                                             - self.prefixSum[row][col]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1] \
                           - self.prefixSum[row2+1][col1]\
                           - self.prefixSum[row1][col2+1]\
                           + self.prefixSum[row1][col1]
    
        # [[0, 0, 0, 0, 0, 0], 
        # [0, 3, 3, 4, 8, 10], 
        # [0, 8, 14, 18, 24, 27], 
        # [0, 9, 17, 21, 28, 36], 
        # [0, 13, 22, 26, 34, 49], 
        # [0, 14, 23, 30, 38, 58]]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)