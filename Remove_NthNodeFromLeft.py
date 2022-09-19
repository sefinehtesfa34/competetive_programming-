# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        counter=0
        while temp:
            counter+=1
            temp=temp.next
        if counter==1:
            return None
        rmvNode=counter-n
        temp=head
        if rmvNode==0:
            head=temp.next
            return head
        while rmvNode>1:
            temp=temp.next
            rmvNode-=1
        if temp.next:
            temp.next=temp.next.next
        return head
            
        
        
        
        
