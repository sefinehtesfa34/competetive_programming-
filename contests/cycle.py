from collections import defaultdict, deque
def find(x):
    if x == parent[x]:
        return x 
    parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    par1 = find(x)
    par2 = find(y)
    if par1 == par2:
        return True 
    parent[par2] = par1 
n, m = list(map(int, input().split()))
graph = []
parent = {}
for _ in range(n):
    path = input()
    graph.append(path)
for row in range(n):
    for col in range(m):
        parent[(row, col)] = (row, col)
def cycle(): 
    for row in range(n):
        for col in range(m):
            if row + 1 < n and graph[row][col] == graph[row + 1][col]:
                if union((row, col), (row + 1, col)):
                    print("Yes")
                    return 
            if col + 1 < m and graph[row][col] == graph[row][col + 1]:
                if union((row, col), (row, col + 1)):
                    print("Yes")
                    return 
    print("No")
cycle()

            


'''
3 4
AAAA
ABCA
AADA

'''
                                
            
    
