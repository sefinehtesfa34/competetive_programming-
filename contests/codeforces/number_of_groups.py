t = int(input())
for _ in range(t):
    n = int(input())
    segments = []
    for _  in range(n):
        segment = list(map(int, input().split()))
        segments.append((segment[1], segment[2], segment[0]))
    segments.sort()
    visited = set()
    def dfs(end, color, index):
        visited.add((end, color))
        if index == len(segments):
            return 1
        segment = segments[index]
        if end >= segment[0] and color != segment[2]:
            visited.add((segment[1], segment[2]))
            if end <= segment[1]:
                color = segment[2]
                end = segment[1]
            return dfs(end, color, index + 1)
        return 1
    counter = 0
    for index, segment in enumerate(segments):
        if (segment[1], segment[2]) not in visited: # (end, color)
            counter += dfs(segment[1], segment[2], index + 1)
    print(counter)
    
    
        
    
        
        