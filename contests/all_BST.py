class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 
class Solution:
    def get_n(self):
        return int(input())
    
    def all_BST(self):
        n = self.get_n()
        all_binary_search_tree = []
    def recursive(self, start, sorted_list):
        if not sorted_list:
            return None 
        
        node = TreeNode(sorted_list[start])
        
        for left in range(len(sorted_list[:start])):
            node.left = self.recursive(left, sorted_list[:start])
        for right in range(len(sorted_list[start + 1:])):
            node.right = self.recursive(right, sorted_list[start + 1:])
        return node 
    

    
        