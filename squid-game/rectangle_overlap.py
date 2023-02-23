class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = [rec1[0], rec1[2]]
        y1 = [rec1[1], rec1[3]]
        x2 = [rec2[0], rec2[2]]
        y2 = [rec2[1], rec2[3]]
        x = sorted([x1, x2])
        y = sorted([y1, y2])
        return x[0][1] > x[1][0] and y[0][1] > y[1][0]
            
        
        
        
        
        
        