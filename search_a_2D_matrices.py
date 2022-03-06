class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                if target in matrix[mid]:
                    return True
                return False
            elif matrix[mid][0]>target:
                right=mid-1
            elif matrix[mid][-1]<target:
                left=mid+1
                
        
            
        
