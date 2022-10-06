from cmath import inf
from collections import defaultdict
from heapq import heapify, heappop, heappush
class Solution:
    def dijkstra(self, startNode, endNode, pathWeight, path, N):
        weights = [inf for _ in range(N)]
        visited = set()
        weights[0] = 0
        heap = [(startNode, 0)]
        heapify(heap)
        while heap:
            currentNode, minWeight = heappop(heap)
            visited.add(currentNode)
            if currentNode == endNode:
                return minWeight 
            for child in path[currentNode]:
                if child in  visited:
                    continue 
                currentWeight = minWeight + pathWeight[(currentNode, child)]
                if currentWeight < weights[child]:
                    weights[child] = currentWeight 
                heappush(heap, (child, weights[child]))
        
solution = Solution()
connections = int(input("Enter the number of connections: "))
N = int(input("Enter the number of nodes : "))
startNode = int(input())
endNode = int(input())
paths = defaultdict(list)
pathWeight = {}
for _ in range(connections):
    path = list(map(int, input().split()))
    paths[path[0]].append(path[1])
    paths[path[1]].append(path[0])
    pathWeight[(path[0], path[1])] = path[2]
    pathWeight[(path[1], path[0])] = path[2]
shortestPath = solution.dijkstra(startNode, endNode, pathWeight, paths, N)
print(shortestPath)
'''             
              0
           10/| \0
           1 9| 2
         6/3\ | /8
         4____3 
            1
0
4
0 1 10
0 2 0
0 3 9
1 4 6
1 3 3
3 4 1
2 3 8
            
            
'''       