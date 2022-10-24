from collections import Counter, defaultdict


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        '''
        case 1:
            each node should have one incoming edge.
        case 2:
            Each edge in the graph should be a directed edge.
        
        The minimu nodes in the graph is one.
        If n is one:
            REUTRN TRUE
        
        Time complexity: O(N) where N is the number of Nodes in the graph
        Space complexity: O(N) where N is the numer of nodes in the graph
        
        '''
        
        indegree = Counter()
        graph = defaultdict(list)
        # I need to check whether the current node has exactly one incoming edge
        for node in range(n):
            if leftChild[node] != -1:
                graph[node].append(leftChild[node])
                indegree[leftChild[node]] += 1
                
            if rightChild[node] != -1:
                indegree[rightChild[node]] += 1
                graph[node].append(rightChild[node])
                
            if indegree[rightChild[node]] >= 2:
                return False
            
            if indegree[leftChild[node]] >= 2:
                return False
        
        # If the graph has more than one disconnected component, it couldn't be a valid BT
        count = 0
        root = None 
        for node in range(n):
            if indegree[node] == 0:
                root = node
                count += 1
            if count == 2:
                return False
        if root == None:
            return False
    
        # If an edge two directions, it will not be a valid BT
        
        def dfs(root, graph, visited):
            if not graph[root]:
                visited.add(root)
                return True

            visited.add(root)
            for child in graph[root]:
                if child in visited:
                    return False
                result = dfs(child, graph, visited)
                if result == False:
                    return False
            return True
        visited = set()
        result = dfs(root, graph, visited)
        if len(visited) < n:
            return False
        
        return result
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        