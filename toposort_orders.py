from collections import Counter, defaultdict


class Solution:
    def toposort(self):
        tasks = self.get_task()
        prerequisites = self.get_relations(tasks)
        graph, indegree = self.get_graph(prerequisites)
        
        def dfs(indegree, path, chosen):
            for task in range(tasks):
                if indegree[task] != 0 or chosen[task]:
                    continue 
                for child in graph[task]:
                    indegree[child] -= 1
                chosen[task] = True 
                path.append(task)
                dfs(indegree, path, chosen)
                if len(path) == tasks:
                    print(path)
                    
                for child in graph[task]:
                    indegree[child] += 1
                chosen[task] = False 
                path.pop()
                
        dfs(indegree, [], defaultdict(bool))
    
    def get_task(self):
        return int(input())
    
    def get_relations(self, tasks):
        prerequisites = []
        for _ in range(tasks):
            prerequisites.append(list(map(int, input().split())))
        return prerequisites 
    
    def get_graph(self, prerequisites):
        indegree = Counter()
        graph = defaultdict(list)
        for pre, suc in prerequisites:
            graph[pre].append(suc)
            indegree[suc] += 1
        return graph, indegree 
    
solution = Solution()
solution.toposort()
'''
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]

'''
