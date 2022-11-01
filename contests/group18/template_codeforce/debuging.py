from collections import defaultdict
 
 
def dfs(node, allowed_consec_cats, parent):
   if allowed_consec_cats < 0:
       return 0
 
   if len(graph[node]) == 1:
       return 1
 
   res = 0
   for neighbour in graph[node]:
       if neighbour == parent:
           continue
      
       if cats[neighbour - 1] == 1:
           res += dfs(neighbour, allowed_consec_cats - 1, node)
       else:
           res += dfs(neighbour, max_allowed_consec_cats, node)
 
   return res
 
 
 
# take input and build
n, max_allowed_consec_cats = map(int, input().split())
cats = list(map(int, input().split()))
graph = defaultdict(list)
 
for _ in range(n-1):
   node1, node2 = map(int, input().split())
   graph[node1].append(node2)
   graph[node2].append(node1)
 
 
#  solve
if cats[0] == 1:
   print(dfs(1, max_allowed_consec_cats - 1, None))
else:
   print(dfs(1, max_allowed_consec_cats, None))