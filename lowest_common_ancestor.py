

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    node=root
    if node is None:
        return None
    if node.info>v1 and node.info>v2:
        return lca(node.left,v1,v2)
    elif node.info<v1 and node.info < v2:
        return lca(node.right,v1,v2)
    else:
        return node
    
    
  #Enter your code here

