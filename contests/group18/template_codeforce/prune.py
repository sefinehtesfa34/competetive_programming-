from collections import *
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def prune(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        graph = {}
        indegree = Counter()
        # Build a graph
        def dfs(current):
            if not current:
                return
            if current.left:
                graph[current.left] = current
                indegree[current] += 1
            if current.right:
                graph[current.right] = current
                indegree[current] += 1
            dfs(current.left)
            dfs(current.right)
            
        dfs(root)
        
        answer = self.topoSort(graph, indegree)
        return answer
    
    def topoSort(self, graph, indegree):
        queue = deque([])
        result = []
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
        while queue:
            size = len(queue)
            cur_ans = []
            for _ in range(size):
                front = queue.popleft()

                cur_ans.append(front.val)
                # if front is the parent node, it don't have any parent
                if front not in graph:
                    break 
                parent = graph[front]
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    queue.append(parent)
            result.append(list(cur_ans))
            
            
        return result
solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8) 
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
print(solution.prune(node1))

    
            
        
        
        
        
        
        
        
        
        
        
                
        