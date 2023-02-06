# class DetectSquares:

#     def __init__(self):
#         self.hashmap = Counter()    
#     def add(self, point: List[int]) -> None:
#         self.hashmap[(point[0], point[1])] += 1 
        
#     def compute(self, x, y, shift_x, shift_y):
#         x_count = self.hashmap[shift_x, y]
#         y_count = self.hashmap[x, shift_y]
#         xy_count = self.hashmap[shift_x, shift_y]
#         return x_count*y_count*xy_count
    
#     def count(self, point: List[int]) -> int:
#         x, y = point
#         ans = 0
#         for index in range(1, 1001):
#             ans += self.compute(x, y, x + index, y + index)
#             ans += self.compute(x, y, x + index, y - index)
#             ans += self.compute(x, y, x - index, y + index)
#             ans += self.compute(x, y, x - index, y - index)
#         return ans
    
# # Your DetectSquares object will be instantiated and called as such:
# # obj = DetectSquares()
# # obj.add(point)
# # param_2 = obj.count(point)
# https://leetcode.com/problems/detect-squares/description/

class DetectSquares:

    def __init__(self):
        self.x_axis = defaultdict(list)
        self.y_axis = defaultdict(list)
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_axis[x].append((x, y))
        self.y_axis[y].append((x, y))
        self.points[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        x1, y1 = point
        squares = 0
        
        for x2, y2 in self.x_axis[x1]:
            side = abs(y2 - y1)
            
            if side == 0:
                continue
                
            if (x1 + side, y1) in self.points and (x2 + side, y2) in self.points:
                squares += self.points[(x1 + side, y1)] * self.points[(x2 + side, y2)]
                
            if (x1 - side, y1) in self.points and (x2 - side, y2) in self.points:
                squares += self.points[(x1 - side, y1)] * self.points[(x2 - side, y2)]
                
        return squares
    