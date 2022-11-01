class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
class Solution:
    def check_palindrome(self, root):
        # Find the mid point
        if not root or not root.next:
            return True 
        mid_node = self.find_half_list(root)
        # Reverse half of the linked list
        half_reversed = self.reverse_list(mid_node)
        # Use two pointers : left pointer and right pointer
        left = root 
        right = half_reversed
        while left != right:
            if left.next == right or right.next == left:
                return left.val == right.val
            
            if left.val != right.val:
                return False 
            left = left.next 
            right = right.next
        return True  
        
        
        # move the two pointer till the mid of the linkedlist
        
        #If the value of left pointer and right pointer is not equal return False
        
        # else finally return True
    def find_half_list(self, root):
        slow = root 
        fast = root.next 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        return slow 
    
    def reverse_list(self, mid_node):
        prev = mid_node 
        next_node = mid_node.next 
        while next_node:
            next = next_node.next 
            next_node.next = prev 
            prev = next_node 
            next_node = next 
        return prev 
    
        
    
        
'''

1 -> 2 -> 3 -> 4 <- 3 <- 2 <- 1
3 -> 2 <- 1
'''

# 1-> 2 -> 3 -> 4 -> 3 -> 2 -> 1
nums = [1,5,6,7,8,7,6,5,1]
head = None 
for num in nums:
    node = ListNode(num)
    if not head:
        head = node
        root = node  
    else:
        head.next = node
        head = node 

solution = Solution()
result = solution.check_palindrome(root)
print(result)
