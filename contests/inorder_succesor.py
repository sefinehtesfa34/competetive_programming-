# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, t):
        self.result = None
        def dfs(root):
            if not root:
                return
            if t >= root.val:
                return dfs(root.right)
            self.result = root
            return dfs(root.left)
        dfs(root)
        return self.result.val
    
        

