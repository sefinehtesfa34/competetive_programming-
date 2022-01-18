# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        self.k=k
        self.l=[]
        self.l2=[]
        counter=0
        if self.k==1:
            return head
        while temp:
            counter+=1
            self.l.append(temp.val)
            temp=temp.next
            if counter%self.k==0:
                self.l2.extend(self.l[::-1])
                self.l=[]
                counter=0
        if  len(self.l)>0:
            self.l2.extend(self.l)
        self.l2=self.l2[::-1]
        head=None
        for i in self.l2:
            node=ListNode(i)
            node.next=head
            head=node
        return head
                
                
                
                
                
                
            
            
        