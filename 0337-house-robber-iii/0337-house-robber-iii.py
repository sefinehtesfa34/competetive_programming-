# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.max_score = 0
        @cache
        def dp(root, turn):
            if not root:
                return 0
            withRoot = (root.val + dp(root.left, False) + dp(root.right, False)) if turn else 0
            withoutRoot = dp(root.left, True) + dp(root.right, True)
            return max(withRoot, withoutRoot)
        return dp(root, True)
    
            
            
            