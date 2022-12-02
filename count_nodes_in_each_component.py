from collections import *
class Solution:
    def find_num_nodes(self):
        graph = defaultdict(list)
        n = int(input())
        edges = int(input())
        parent = {index:index for index in range(n)}
        self.size = {index:1 for index in range(n)}
        for _ in range(edges):
            left, right = list(map(int, input().split()))
            graph[left].append(right)
            graph[right].append(left)
        for node in graph:
            for child in graph[node]:
                self.union(parent, node, child)
        processed = set()
        for node in graph:
            cur_parent = self.find(parent, node)
            if cur_parent not in processed:
                print(self.size[cur_parent])
                processed.add(cur_parent)
        
    def find(self, parent, x):
        while x != parent[x]:
            x = parent[x]
        return x 
    
    def union(self, parent, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent,  y)
        if x_parent != y_parent:
            if self.size[x_parent] > self.size[y_parent]:
                x_parent, y_parent = y_parent, x_parent 
            parent[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        
solution = Solution() 
solution.find_num_nodes()
