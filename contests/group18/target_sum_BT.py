from collections import defaultdict


class Solution:
    def __init__(self):
        self.number_of_paths = 0
        
    def target_sum(self):
        target = self.get_target()
        graph = self.get_graph()
        
    def dfs(self, current_node, target, graph, sums = set()):
        if not graph[current_node]:
            return current_node 
        
        
        
        
        
    def get_target(self):
        return int(input())
    
    def get_graph(self):
        number_of_edges = int(input())
        number_of_vertices = int(input())
        graph = defaultdict(list)
        for _ in range(number_of_edges):
            parent, child = list(map(int, input().split()))
            graph[parent].append(child)
        return graph 
    
        
        
        