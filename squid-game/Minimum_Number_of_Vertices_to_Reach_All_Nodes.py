class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = [False]*n
        for left, right in edges:
            reachable[right] = True
        return [index for index in range(n) if reachable[index] == False]
    