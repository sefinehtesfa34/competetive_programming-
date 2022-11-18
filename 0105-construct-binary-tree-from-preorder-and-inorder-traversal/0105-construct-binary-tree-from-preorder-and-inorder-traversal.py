# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = preorder[::-1]
        def build(inorder):
            
            if not inorder or not preorder:
                return None
            root = TreeNode(preorder[-1])
            index = inorder.index(preorder[-1])
            preorder.pop()
            root.left = build(inorder[:index])
            root.right = build(inorder[index + 1:])
            return root
        
        return build(inorder)
    