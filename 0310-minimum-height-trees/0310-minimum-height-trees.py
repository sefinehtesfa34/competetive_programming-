class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = Counter()
        queue = deque([])
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
            indegree[left] += 1
            indegree[right] += 1
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)
        # visited = set()
        while n > 2:
            size = len(queue)
            n -= size
            for _ in range(size):
                front = queue.popleft()
                # visited.add(front)
                for depend in graph[front]:
                    indegree[depend] -= 1
                    if indegree[depend] == 1:
                        queue.append(depend)
        
        return queue
    
                    