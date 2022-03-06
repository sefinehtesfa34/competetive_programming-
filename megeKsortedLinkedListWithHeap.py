# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values=[]
        output=[]
        for i in range(len(lists)):
            temp=lists[i]
            while temp:
                hq.heappush(values,temp.val)
                temp=temp.next
        for i in range(len(values)):
            output.append(hq.heappop(values))
        head=None
        for i in output[::-1]:
            node=ListNode(i)
            node.next=head
            head=node
        return head
            
            
