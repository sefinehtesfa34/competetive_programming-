# all task scheduling algorithm
from collections import deque
class Solution:
    def printOrders(self, tasks, prerequisites):
        # Write your code here
        if tasks <= 0:
            return []
        # build graph
        graph = {i:[] for i in range(tasks)}
        indegree = {i:0 for i in range(tasks)}  
        for parent, child in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1

        # find all sources
        queue = deque()
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        # find all permutations
        result = []
        self.findPermutations(graph, indegree, queue, [], result)
        return result
    def findPermutations(self, graph, indegree, queue, path, result):
        if queue:
            for vertex in queue:
                path.append(vertex)
                queueCopy = deque(queue) # make a copy of queue 
                queueCopy.remove(vertex)
                for child in graph[vertex]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queueCopy.append(child)
                # recursive call to print other orderings from the remaining (and new) sources
                self.findPermutations(graph, indegree, queueCopy, path, result)
                # backtrack, remove the vertex from the path to try other orderings
                path.pop()
                # put the child back for the next permutation
                for child in graph[vertex]:
                    indegree[child] += 1
        # if queue is empty, all vertices are in the path, so print the path
        if len(path) == len(indegree):
            result.append(path[:])
sol = Solution()

print(sol.printOrders(3, [[0, 1], [1, 2]]))
print(sol.printOrders(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))  
print(len(sol.printOrders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))