from collections import *
def toposort(graph, n, start):
    indegree = Counter()
    queue = deque()
    dp = [1]*n
    for node in graph:
        for child in graph[node]:
            indegree[child] += 1
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)
    while queue:
        front = queue.popleft()
        for child in graph[front]:
            dp[child] = max(dp[child], 1 + dp[front])
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    print(dp)
    return max(dp)
n = 8
graph = {0:[1, 2], 1:[4], 2:[3], 3:[1, 4, 5], 4:[6,5], 5:[6], 6:[7], 7:[]}
print(toposort(graph, n, 0))
