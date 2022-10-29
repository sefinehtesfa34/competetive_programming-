# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import Counter
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.answer = 0
        self.dfs(root, targetSum)
        return self.answer
    
    def dfs(self, current, targetSum, cur_sum = 0, hashmap = Counter([0])):
        if not current:
            return 
        cur_sum += current.val
        self.answer += hashmap[cur_sum - targetSum]
        hashmap[cur_sum] += 1
        