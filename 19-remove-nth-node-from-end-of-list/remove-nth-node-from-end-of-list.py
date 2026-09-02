# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ACCEPTED BUT REQUIRED 3 full passes
        # prev=None
        # curr=head
        # while curr:
        #     tmp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=tmp
        # curr=prev
        # head=prev
        # # print(curr)
        # prev=None
        # c=1
        # while curr:
        #     if(c==n):
        #         if(prev==None):
        #             head=head.next
        #             break
        #         prev.next=curr.next
        #         break
        #     prev=curr
        #     curr=curr.next
        #     c+=1
        # prev=None
        # curr=head
        # while curr:
        #     tmp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=tmp
        # return prev

        # 2 pointer approach
        dummy=ListNode(0,head)
        p1=dummy
        p2=head

        for _ in range(n):
            # if(p2):
            #     print(p2.val)
            # else:
            #     print("Nowdwedne")
            p2=p2.next
            
        while p2:
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
        return dummy.next
