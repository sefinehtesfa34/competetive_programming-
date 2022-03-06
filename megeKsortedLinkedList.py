# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listValues=[]
        for temp in lists:
            while temp:
                listValues.append(temp.val)
                temp=temp.next
        listValues.sort()
        head=None
        for i in listValues[::-1]:
            node=ListNode(i)
            node.next=head
            head=node
        return head
