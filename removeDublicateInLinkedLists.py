# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp:
            if temp.val not in lst:
                lst.append(temp.val)
            temp=temp.next
        head=None
        for i in lst[::-1]:
            newNode=ListNode(i)
            newNode.next=head
            head=newNode
        return head