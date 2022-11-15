class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.size = {(x, y):1 for x, y in stones}
        parent = {(x, y):(x, y) for x, y in stones}
        visited = set()
        result = 0
        for index in range(len(stones)):
            for curr in range(index + 1, len(stones)):
                if stones[index][0] == stones[curr][0] or stones[index][1] == stones[curr][1]:
                    self.union(parent, tuple(stones[index]), tuple(stones[curr]))
        for x, y in stones:
            parent_point = self.find(parent, (x, y))
            if parent_point not in visited:
                result += self.size[parent_point] - 1
            visited.add(parent_point)
            
        return result
    
        
    def find(self, parent, point):
        if point == parent[point]:
            return point
        parent[point] = self.find(parent, parent[point])
        return parent[point]
    
    def union(self, parent, point1, point2):
        parent_point1 = self.find(parent, point1)
        parent_point2 = self.find(parent, point2)
        if parent_point1 != parent_point2:
            if self.size[parent_point1] < self.size[parent_point2]:
                parent_point1,parent_point2 = parent_point2, parent_point1
                
            parent[parent_point2] = parent_point1
            self.size[parent_point1] += self.size[parent_point2]
    
        
        
        '''
                    |                    
                    *--------*   
                    |   *      
____________________*---------*______________________
                    |
                    |
                    |
                    |
                    |
        
        
        '''