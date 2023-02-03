# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        maper = defaultdict(list)
        def dfs(root, row, col):
            if not root:
                return 
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            maper[col].append((row, root.val))
        dfs(root, 0, 0)
        result = list(map(lambda x:sorted(x[1]), sorted(maper.items())))
        answer = []
        for res in result:
            filtered = list(map(lambda x:x[1], res))
            answer.append(filtered)
        return answer
        
        
        
                
        
            