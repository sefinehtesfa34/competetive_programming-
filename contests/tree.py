from collections import Counter, defaultdict, deque
t = int(input())
for _ in range(t):
    input()
    n, k = list(map(int, input().split()))
    graph = defaultdict(list)
    indegree = Counter()
    visited = set()
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
        indegree[a] +=1
        indegree[b] += 1
    queue = deque()
    for node in graph:
        if indegree[node] == 1:
            queue.append(node)
    count = 0
    level = 0
    while queue:
        if level == k:
            break 
        level += 1
        size = len(queue)
        count += size 
        for _ in range(size):
            cur = queue.popleft()
            visited.add(cur)
            for child in graph[cur]:
                if child in visited:
                    continue
                indegree[child] -= 1
                if indegree[child] == 1:
                    queue.append(child)
    
    if n == 1:
        if k >= 1:
            print(0)
        else:
            print(n)
    else:
        print(n - count)

    