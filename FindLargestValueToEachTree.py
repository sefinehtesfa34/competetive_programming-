# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        queue.append(root)
        output=[]
        if not root:
            return
        while queue:
            max_val=-inf
            size=len(queue)
            for i in range(size):
                top =queue.popleft()
                if top.val>max_val:
                    max_val=top.val
                if top.left is not None:
                    queue.append(top.left)
                if top.right is not None:
                    queue.append(top.right)
            output.append(max_val)
        return output
            
                
