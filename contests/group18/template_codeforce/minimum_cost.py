from os import *
from sys import *
from collections import *
from math import *
from heapq import *

def getMinimumCost(n, m, connections):
    parent  = {node:node for node in range(1, n + 1)}
    size = [1]*(n)
    connections.sort(key = lambda x:x[2])
    
    def find(node):
        while node != parent[node]:
            node = parent[node]
        return node
    
    def union(node1, node2):
        par_node1 = find(node1)
        par_node2 = find(node2)
        if size[par_node1 - 1] < size[par_node2 - 1]:
            par_node1, par_node2 = par_node2, par_node1
        size[par_node1 - 1] += size[par_node2 - 1]
        parent[par_node2] = par_node1
        
    total_cost = 0
    for node1, node2, weight in connections:
        if find(node1) != find(node2):
            total_cost += weight
            union(node1, node2)
    all_connected_nodes = find(1)
    if all_connected_nodes < n:
        return -1
    return total_cost


n,m = list(map(int, input().split()))
connections = []
for _ in range(m):
    node1, node2, weight = list(map(int, input().split()))
    connections.append((node1, node2, weight))

result = getMinimumCost(n, m, connections)
print(result)


        
        
        
    
    

        
        
        
        
        
        
        
        
        
        
        
        
    