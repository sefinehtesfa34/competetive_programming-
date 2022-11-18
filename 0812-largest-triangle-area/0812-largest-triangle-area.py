class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a = sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1])**2)
                for k in range(j + 1, len(points)):
                    b = sqrt((points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1])**2)
                    c = sqrt((points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1])**2)
                    s = (a + b + c) / 2
                    print(s*(s - a) * (s - b) * (s - c))
                    cur_area = sqrt(max(0, s*(s - a) * (s - b) * (s - c)))
                    area = max(area, cur_area)
        return area
    
        
        
        
        
        
        
        
        