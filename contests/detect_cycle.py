from collections import defaultdict, deque
def isBound(row, col):
    return 0 <= row < n and 0 <= col < m 

n, m = list(map(int, input().split()))
graph = []
parent = defaultdict()
for _ in range(n):
    path = input()
    graph.append(path)
visited = set()
def dfs(row, col, prev):
    visited.add((row, col))
    for neighbor in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newRow, newCol = row + neighbor[0], col + neighbor[1]
        child = (newRow, newCol)
        if isBound(newRow, newCol) and graph[row][col] == graph[newRow][newCol]:
            if child in visited:
                if child != prev:
                    return True 
            else:
                if dfs(newRow, newCol, (row, col)):
                    return True 
    return False
result = 'No' 
for row in range(n):
    for col in range(m):
        if (row, col) not in visited:
            if dfs(row, col, (row, col)):
                result = "Yes"
                break
    if result == "Yes":
        break 
print(result)        
         
