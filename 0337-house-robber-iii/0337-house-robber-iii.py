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
            #rob the root
            withRoot = withoutRoot = 0
            if turn:
                withRoot = root.val + dp(root.left, False) + dp(root.right, False)
            withoutRoot = dp(root.left, True) + dp(root.right, True)
            
            # pass the root and rob the next level houses
            return max(withRoot, withoutRoot)
        return dp(root, True)
    
            
            
            