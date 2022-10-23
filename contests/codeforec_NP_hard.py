from collections import defaultdict
class Solution:
    def isBipartite(self, graph, n) -> bool:
        colors = [-1]*n
        for node in range(1, n + 1):
            if colors[node - 1] == -1:
                colors[node - 1] = 0
                result = self.dfs(node, graph, colors)
                if not result:
                    return -1
        return colors
    
    def dfs(self, current, graph, colors):     
        for neighbor in graph[current]:
            if colors[neighbor - 1] == colors[current - 1]:
                return False 
            colors[neighbor - 1] = int(not colors[current - 1])
            if colors[neighbor] == -1:
                result = self.dfs(neighbor, graph, colors)
                if result == False :
                    return False 
        return True

def get_graph(n, m):
    graph = defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        graph[v].append(u)
        graph[u].append(v)
    return graph 
    
def main():
    n, m = list(map(int, input().split()))
    graph = get_graph(n, m)
    solution = Solution()
    result = solution.isBipartite(graph, n)
    if result == -1:
        return print(result)
    group1 = group2 = 0
    set_a = set()
    set_b = set()
    for index in range(len(result)):
        if result[index] == 0:
            group1 += 1
            set_a.add(index + 1)
        elif result[index] == 1:
            group2 += 1
            set_b.add(index + 1)
    print(group1)
    print(*set_a)
    print(group2)
    print(*set_b)
main()

import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()