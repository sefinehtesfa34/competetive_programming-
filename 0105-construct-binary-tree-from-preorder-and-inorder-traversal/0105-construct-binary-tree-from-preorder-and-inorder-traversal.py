# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pointer = 0 
        hashmap = {val:index for index, val in enumerate(inorder)}
        
        def build(start, end):
            nonlocal pointer
            if start > end:
                return None
            
            root = TreeNode(preorder[pointer])
            pointer += 1
            root.left = build(start, hashmap[root.val] - 1)
            root.right = build(hashmap[root.val] + 1, end)
            return root
        
        
        return build(0, len(inorder) - 1)
    