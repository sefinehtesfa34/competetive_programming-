from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLength = 0
        def isUnique(string,visited):
            if len(string) != len(set(string)):
                return False
            visited = set(visited)
            for char in string:
                if char in visited:
                    return False
            return True
        def dfs(index, visited):
            nonlocal maxLength
            maxLength = max(maxLength, len(visited))
            if index == len(arr):
                return
            if isUnique(arr[index], visited):
                dfs(index + 1, visited + arr[index])
            dfs(index + 1, visited)
        dfs(0, '')
        return maxLength
    