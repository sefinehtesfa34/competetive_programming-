# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, root: Optional[ListNode]) -> int:
        if not root or not root.next:
            return True 
        mid_node = self.find_half_list(root)
        # Reverse half of the linked list
        half_reversed = self.reverse_list(mid_node)
        # Use two pointers : left pointer and right pointer
        left = root 
        right = half_reversed
        max_score = 0
        while left.next != right:
            max_score = max(max_score, left.val + right.val) 
            left = left.next 
            right = right.next
        max_score = max(max_score, left.val + right.val)
        return max_score
        
        
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