class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = Counter()
        result  = defaultdict(set)
        queue = deque([])
        for left, right in edges:
            indegree[right] += 1
            graph[left].append(right)
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
        while queue:
            front = queue.popleft()
            for children in graph[front]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    queue.append(children)
                result[children] = result[children].union(result[front])
                result[children] = result[children].union({front})
        answer = []
        for node in range(n):
            answer.append(sorted(result[node]))
        return answer
    