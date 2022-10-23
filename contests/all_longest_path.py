from cmath import inf
from collections import defaultdict


class Solution:
    def all_longest_path(self, current_node):
        graph = defaultdict(list)
        store = defaultdict(dict)
        vertices = int(input())
        edges = int(input())
        for _ in range(edges):
            vertix1, vertix2  = list(map(int, input().split()))
            graph[vertix1].append(vertix2)
            graph[vertix2].append(vertix1)
        self.longest_path(graph, current_node, store)
        return store 
    
    def longest_path(self, graph, current_node, store, visited = set()):
        # store could be dict of dict.
        # Like hashmap = {key:{key1:24, key2:67, key3:89},anotherkey:{......}, .....}
        if current_node in visited:
            return -1
        
        visited.add(current_node)
        max_length = 0
        for child in graph[current_node]:
            max_length = max(max_length, 1 + self.longest_path(graph, child, store))
            for another_child in graph[current_node]:
                if another_child != child:
                    if another_child not in store[current_node]:
                        store[current_node][another_child] = max_length
                    else:
                        store[current_node][another_child] = max(store[current_node][another_child], max_length)
        return max_length 
        


solution = Solution()
result = solution.all_longest_path(1)
print(result)