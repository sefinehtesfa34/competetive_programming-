from cmath import inf
from collections import defaultdict


class Solution:
    def dfs(self, current, graph, memo, visited = set()):
        if len(graph[current]) == 1 and graph[current][0] in visited:
            return 1
        
        visited.add(current)
        counter = 0
        for child in graph[current]:
            if child not in visited:
                counter += self.dfs(child ,graph, memo, visited)
        
        memo[current] = counter
        return 1 + memo[current]
    
    def find_max(self, memo, graph, current, answer, visited):
        
        if len(graph[current]) == 1 and graph[current][0] in visited:
            return 
        if len(graph[current]) == 1:
            answer[0] += memo[graph[current][0]]
            return
         
        visited.add(current)
        current_max = 0
        min_node = -1
        cur_min = inf
        for child in graph[current]:
            if child not in visited:
                current_max = max(current_max, memo[child])
                if memo[child] < cur_min:
                    min_node = child 
                    cur_min = memo[child]
        if min_node == -1:
            return 
        answer[0] += current_max 
        self.find_max(memo, graph, min_node,answer, visited)
        
    
    def infected_tree(self):
        test = int(input())
        for _ in range(test):
            n = int(input())
            graph = defaultdict(list)
            for _ in range(n - 1):
                vertix1, vertix2 = list(map(int, input().split()))
                graph[vertix1].append(vertix2)
                graph[vertix2].append(vertix1)
            memo = [0 for _ in range(n + 1)]
            self.dfs(1, graph, memo, set())
            answer = [0]
            self.find_max(memo, graph, 1, answer, set())
            print(answer[0])
def main():
    solution = Solution()
    solution.infected_tree()

import sys
import threading
sys.setrecursionlimit(1<<30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
# main()
      
