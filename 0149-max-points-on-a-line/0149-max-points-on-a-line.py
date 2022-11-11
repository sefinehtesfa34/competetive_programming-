class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
            if len(points) <= 2:
                return len(points)
            max_points = 2
            for index_i in range(len(points)):
                for index_j in range(index_i +1, len(points)):
                    x1 = points[index_i][0]
                    y1 = points[index_i][1]
                    x2 = points[index_j][0]
                    y2 = points[index_j][1]
                    if x1 != x2:
                        m =(y2 - y1)/(x2 - x1)
                    else:
                        m = None
                    counter = 2
                    for index in range(index_j + 1, len(points)):
                        x = points[index][0]
                        y = points[index][1]
                        if m == None:
                            if x == x1:
                                counter += 1
                        else:
                            if x == x1:
                                continue
                            slope = (y1 - y)/(x1 - x)
                            if slope == m:
                                counter += 1
                    max_points = max(max_points, counter)
            return max_points




         
       
