# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class DListNode:
    def __init__(self, val=0, prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        # dummy=ListNode(0,head)
        d_dummy=DListNode()
        d_dummy.next=DListNode(head.val)
        d_dummy.next.prev=d_dummy
        curr=head.next
        tail=d_dummy.next
        while(curr):
            curr2=tail
            # print(curr.val)
            while(curr2.val>curr.val and curr2!=d_dummy):
                curr2=curr2.prev
            nn=DListNode(curr.val,curr2,curr2.next)
            if(curr2.next):
                tmp=curr2.next
                tmp.prev=nn
            else:
                tail=nn
            curr2.next=nn
            curr=curr.next
        c=d_dummy
        while(c):
            # print(c.val, end="<=>")
            c=c.next
        # print()
        # print(d_dummy)
        # res=ListNode()
        # t=res
        
        res = ListNode()  # Dummy head
        d_dummy=d_dummy.next
        t = res           # Pointer used to build the list

        while d_dummy:
            # print(d_dummy.val)
            t.next = ListNode(d_dummy.val)
            t = t.next
            d_dummy = d_dummy.next
            
        return res.next