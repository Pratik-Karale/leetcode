# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        curr=prev
        head=prev
        # print(curr)
        prev=None
        c=1
        while curr:
            if(c==n):
                if(prev==None):
                    head=head.next
                    break
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
            c+=1
        prev=None
        curr=head
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        return prev
