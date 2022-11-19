class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        max_length = 0
        for first in words:
            for next in words:
                if len(next) - 1 == len(first):
                    graph[first].append(next)
        
        def is_chain(first, next):
            left = right =0
            while left < len(first) and right < len(next):
                if next[right] == first[left]:
                    left += 1
                    right += 1
                else:
                    right += 1
            return left == len(first) and (right == len(next) or right == len(next) - 1)
        memo = {}
        def dfs(start, visited):
            if start in memo:
                return memo[start]
            visited.add(start)
            length = 0
            for child in graph[start]:
                if child in visited or not is_chain(start, child):
                    continue
                length = max(length, 1 + dfs(child, visited))
            memo[start] = length
            return length
        
        for word in words:
            max_length = max(max_length, 1 + dfs(word, set()))
        return max_length
    
        
        
        
        
        
        
        
        
        
            