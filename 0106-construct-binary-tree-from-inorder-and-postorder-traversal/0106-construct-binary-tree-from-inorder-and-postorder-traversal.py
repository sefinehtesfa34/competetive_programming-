# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pointer = len(postorder) - 1
        def build(inorder):
            nonlocal pointer
            if not inorder or pointer < 0:
                return None
            
            root = TreeNode(postorder[pointer])
            index = inorder.index(postorder[pointer])
            pointer -= 1
            root.right = build(inorder[index + 1:])
            root.left = build(inorder[:index])
            return root
        
        return build(inorder)
            
            
            
            
            
            
            