class Node:
    def __init__(self, val):
        self.left = None 
        self.right = None 
        self.val = val 
        self.leftSubTree = 0
class Solution:
    def __init__(self, nums) -> None:
        self.root = Node(nums[0])
        for num in nums[1:]:
            currentNode = Node(num)
            self.root = self.insert(self.root, self.root, currentNode)
        self.leftSubtree(self.root, self.root)
        print(self.root.leftSubTree)
    def insert(self, cur, root, currentNode):
        if not root.left and currentNode.val <= root.val:
            root.left = currentNode
            return cur  
        if not root.right and currentNode.val > root.val:
            root.right = currentNode 
            return cur 
        if root.val >= currentNode.val:
            return self.insert(cur, root.left, currentNode)
        return self.insert(cur, root.right, currentNode)
    def leftSubtree(self, cur, root):
        if not root:
            return 0
        root.leftSubTree = self.leftSubtree(cur, root.left)
        self.assign(cur)
        return 1 + self.leftSubtree(cur, root.left) + self.leftSubtree(cur, root.right)
    def assign(self, root):
        self.root = root 
    
    '''
         3
        / \
       3   4
      /  \
      1   2
    '''
        
        
    def rankFromStream(self, nums):
        pass 
nums = list(map(int, input().split()))
solution = Solution(nums)
result = solution.root 
def printNode(root):
    if not root:
        return 
    
    printNode(root.left)
    print(root.val, end = ' ')
    printNode(root.right)
printNode(result)

