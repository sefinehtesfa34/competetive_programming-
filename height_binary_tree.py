

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root is None:
        return -1
    else:
        left=height(root.left)
        right=height(root.right)
        if left>right:
            return left+1
        else:
            return right+1
   

