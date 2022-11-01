# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = -inf
        return self.dfs(root)
    
    def dfs(self, current):
        if not current:
            return True
        left = self.dfs(current.left)
        if current.val <= self.prev:
            return False
        self.prev = current.val
        right = self.dfs(current.right)
        
        return left and right
    
        