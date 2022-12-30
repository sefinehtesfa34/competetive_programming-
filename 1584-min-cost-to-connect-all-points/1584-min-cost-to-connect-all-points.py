class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = {index:1 for index in range(len(points))}
        parent = {node:node for node in range(len(points))}
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(x, y):
            x_parent = find(x)
            y_parent = find(y)
            if x_parent != y_parent:
                if size[x_parent] < size[y_parent]:
                    x_parent, y_parent = y_parent, x_parent
                parent[y_parent] = x_parent
                size[x_parent] += size[y_parent]
                
        edges = []
        answer = 0
        for index in range(len(points)):
            for curr in range(index + 1, len(points)):
                weight = abs(points[index][0] - points[curr][0]) + abs(points[index][1] - points[curr][1])
                edges.append([weight, index, curr])
        sorted_edges = sorted(edges)
        for weight, left,right in sorted_edges:
            if find(left) != find(right):
                answer += weight
                union(left, right)
        return answer
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        