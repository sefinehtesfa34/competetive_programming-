# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pointer = 0 
        def build(inorder):
            nonlocal pointer
            if not inorder or pointer == preorder:
                return None
            
            root = TreeNode(preorder[pointer])
            index = inorder.index(preorder[pointer])
            pointer += 1
            root.left = build(inorder[:index])
            root.right = build(inorder[index + 1:])
            return root
        
        
        return build(inorder)
    