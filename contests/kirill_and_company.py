from cmath import inf
from collections import defaultdict
t = int(input())
graph = defaultdict(list)
def dp(root,dest):
    if root == dest:
        return 0
    minPath = inf
    for child in graph[root]:
        minPath = 1 + min(minPath, dp(child, dest))
        
    return minPath 


'''
dp = [inf]*(n)
dp[1] = 0
dp[root] = 1 + min(dp[root], dp[child])

      3
      
      
     / \ 
    1   5
     \
       2
 '''
 
