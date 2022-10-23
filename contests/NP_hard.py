from collections import defaultdict, deque


class Solution:
    def bfs(self, graph, vertices, edges):
        graph = self.get_graph(vertices, edges)
        colors = [-1]*vertices 
        for node in range(vertices):
            if colors[node - 1] == -1:
                queue = deque([node])
            while queue:
                front = queue.popleft()
                for neighbor in graph[front]:
                    if colors[neighbor - 1] == colors[front - 1]:
                        print(-1)
                        exit()
                    if colors[neighbor - 1] == -1:
                        colors[neighbor - 1] = 1 - colors[front - 1]
                        queue.apend(neighbor)
        return colors 

                            
    def get_graph(self, n, m):
        graph = defaultdict(list)
        for _ in range(m):
            u, v = list(map(int, input().split()))
            graph[v].append(u)
            graph[u].append(v)
        return graph 
def main():
    n, m = list(map(int, input().split()))
    solution = Solution()
    graph = solution.get_graph(n, m)
    result = solution.bfs(graph, n, m)
    group1 = group2 = 0
    set_a = set()
    set_b = set()
    for index in range(len(result)):
        if result[index] == 0:
            group1 += 1
            set_a.add(index + 1)
        else:
            group2 += 1
            set_b.add(index + 1)
    print(group1)
    print(*set_a)
    print(group2)
    print(*set_b)
main()
