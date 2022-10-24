class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
class Solution:
    def make_BST(self):
        sorted_list = self.get_sorted_list()
        root = self.recursive(sorted_list)
        stack = []
        while root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            print(root.val)
            while not root.right and stack:
                root = stack.pop()
                print(root.val)
            root = root.right 
             
             
            

    def get_sorted_list(self):
        return list(map(int, input().split()))
    
    def recursive(self, sorted_list):
        #If the array or list is empty return None
        if not sorted_list:
            return None 
        #Find the mid number 
        mid = len(sorted_list)//2
        
        # Create a TreeNode
        current_node = TreeNode(sorted_list[mid])
        #right subtree and left subtree
        current_node.left = self.recursive(sorted_list[:mid])
        current_node.right = self.recursive(sorted_list[mid + 1:])
        
        return current_node 
solution = Solution()
solution.make_BST()

        