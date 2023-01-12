class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        answer = [0]*n
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        def dfs(current, parent):
            ans = [0]*26
            ans[ord(labels[current]) - ord('a')] = 1
            for child in graph[current]:
                if child != parent:
                    child_response = dfs(child, current)
                    for index in range(26):
                        ans[index] += child_response[index]
            answer[current] = ans[ord(labels[current]) - ord('a')]
            return ans
        dfs(0, -1)
        return answer
    
        