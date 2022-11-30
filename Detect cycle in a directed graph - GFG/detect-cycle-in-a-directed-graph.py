#User function Template for python3

from collections import *
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = set()
        indegree = Counter()
        graph = defaultdict(list)
        starter = []
        for index in range(len(adj)):
            for curr in adj[index]:
                graph[index].append(curr)
                indegree[curr] += 1
        for node in range(V):
            if indegree[node] == 0:
                starter.append(node)
        colors = [-1]*V
        if not starter:
            return True
        def dfs(node):
            if colors[node] == 1:
                return True
                
            if colors[node] == 2:
                return False
                
            colors[node] = 1
            for child in graph[node]:
                has_cycle = dfs(child)
                if has_cycle:
                    return True
            colors[node] = 2
            return False
            
        for node in starter:
            if dfs(node):
                return True
        return False
        
            
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends