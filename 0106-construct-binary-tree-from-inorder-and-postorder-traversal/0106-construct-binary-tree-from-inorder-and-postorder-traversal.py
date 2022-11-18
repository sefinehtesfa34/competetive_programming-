# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pointer = len(postorder) - 1
        hashmap = {val:index for index, val in enumerate(inorder)}
        def build(start, end):
            nonlocal pointer
            if start > end:
                return None
            root = TreeNode(postorder[pointer])
            pointer -= 1
            root.right = build(hashmap[root.val] + 1, end)
            root.left = build(start, hashmap[root.val] - 1)
            return root
        
        return build(0, len(inorder) - 1)
    
            
            
            
            
            
            
            