# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        carry=0
        while temp1 or temp2:
            if temp1:
                if temp2:
                    data=temp1.val+temp2.val+carry
                    if data>=10:
                        carry=1
                        data=data%10
                    else:
                        carry=0
                    temp2=temp2.next
                else:
                    data=temp1.val+carry
                    if data>=10:
                        data=data%10
                        carry=1
                    else:
                        carry=0
                self.linkedList(data)
                temp1=temp1.next
            elif temp2:
                if temp1:
                    data=temp1.val+temp2.val+carry
                    if data>=10:
                        carry=1
                        data=data%10
                    else:
                        carry=0
                    temp1=temp1.next
                else:
                    data=temp2.val+carry
                    if data>=10:
                        data=data%10
                        carry=1
                    else:
                        carry=0
                self.linkedList(data)
                temp2=temp2.next
        if carry==1:
            self.linkedList(carry)
        return self.head
    def linkedList(self,data):
        node=ListNode(data)
        if not self.head:
            self.head=node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
