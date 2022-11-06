# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]
        self.dfs(max_sum, root)
        return max_sum[0]

    def dfs(self, max_sum, root):
        if not root:
            return 0
        left = max(0, self.dfs(max_sum, root.left))
        right = max(0, self.dfs(max_sum, root.right))
        
        max_sum[0] = max(max_sum[0], root.val + left + right)
        return root.val + max(left, right)

        

	
	
		