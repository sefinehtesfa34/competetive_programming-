from collections import defaultdict


n, m = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
group1 = set()
group2 = set()
answer  =[]
def dfs(root, parent, visited  = set()):
    for child in graph[root]:
        if child == parent:
            continue
        if child  in group1 or child  in group2:
            if not answer :
                answer.append(-1)
            return
        if parent in group1:
            group2.add(child)
        else:
            group1.add(child)
            group2.add(parent)
        dfs(child, root, visited)
    return
for node in graph:
    group2.add(node)
    dfs(node, node)
    break 
if not answer:
    print(len(group1))
    for node in group1:
        print(node, end = " ")
    print()
    print(len(group2))
    for node in group2:
        print(node, end = ' ')
else:
    print(answer[0])

    
        
'''
1 <-> 2 <-> 3
3 -> 1
{2}
{1,3}

'''

