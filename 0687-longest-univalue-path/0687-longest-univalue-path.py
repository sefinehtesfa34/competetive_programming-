class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(parent, root):
            if not root:return 0
            left = dfs(root.val, root.left)
            right = dfs(root.val, root.right)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if root.val == parent else 0
        dfs(None, root)
        return self.longest
    
        