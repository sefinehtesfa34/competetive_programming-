from string import ascii_lowercase
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        dp = [[0]*26 for _ in range(n + 1)]
        orders = []
        queue = deque([0])
        visited = set() 
        while queue:
            size = len(queue)
            for _ in range(size):
                front = queue.popleft()
                visited.add(front)
                orders.append(front)
                for child in graph[front]:
                    if child not in visited:
                        queue.append(child)
        orders = orders[::-1]
        for current in orders:
            for child in graph[current]:
                for index in range(26):
                    dp[current][index] += dp[child][index]
            
            dp[current][ord(labels[current]) - ord('a')] += 1
        output = [dp[index][ord(labels[index]) - ord('a')] for index in range(n)]
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        