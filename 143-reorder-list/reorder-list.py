# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p2=head
        p1=head
        while p2 and p2.next:
            # print(p1.val)
            p1=p1.next
            p2=p2.next.next
        
        prev=None
        while p1:
            tmp=p1.next
            p1.next=prev
            prev=p1
            p1=tmp
            # print(prev.val)
        s=prev
        f=head
        while s.next:
            # print("  ",head,"\n-----")
            tmp1=f.next
            tmp2=s.next
            f.next=s
            s.next=tmp1
            f=tmp1
            s=tmp2
        




        