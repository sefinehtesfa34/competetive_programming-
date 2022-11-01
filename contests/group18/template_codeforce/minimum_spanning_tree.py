from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def spanning_tree(self):
        vertices, edges = list(map(int, input().split()))
        parent = {node:node for node in range(1, vertices + 1)}
        # Build a weighted graph
        graph = self.get_graph(edges)
        #Use kruskal's algorithm
        #Use a a priotity queue is helpful here
        heap_queue = []
        spanning_tree = defaultdict(list)
        for node in graph:
            for child in graph[node]:
                heappush(heap_queue, (child[1], node, child[0]))
        
        while heap_queue:
            _, node1, node2 = heappop(heap_queue)
            is_cycle = self.union(parent, node1, node2)
            if not is_cycle:
                spanning_tree[node1].append(node2)
                spanning_tree[node2].append(node1)
        return print(spanning_tree)
    
    def find(self, parent, node):
        while node != parent[node]:
            node = parent[node]
        return node 
    
    def union(self, parent, node1, node2):
        node1_parent = self.find(parent, node1)
        node2_parent = self.find(parent, node2)
        if node1_parent == node2_parent:
            return True 
        parent[node1_parent] = node2_parent 
        return False 
    
    def get_graph(self, edges):
        graph = defaultdict(list)
        for _ in range(edges):
            node1, node2, weight = list(map(int, input().split()))
            graph[node1].append((node2, weight))
            graph[node2].append((node1, weight))
        return graph 
solution = Solution()
solution.spanning_tree()
'''
                1
             /     \  
            4        3
          /           \
        6              5
                     /   \
                    7      2
                    
                        
                        
                        
'''