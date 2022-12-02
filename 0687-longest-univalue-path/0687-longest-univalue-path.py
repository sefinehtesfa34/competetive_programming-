# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(parent, root):
            if not root:
                return 0
            left = dfs(root.val, root.left)
            right = dfs(root.val, root.right)
            self.longest = max(self.longest, left + right)
            if root.val == parent:
                return 1 + max(left, right)
            return 0
        
        dfs(None, root)
        return self.longest
    
        