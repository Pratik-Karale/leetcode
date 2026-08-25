# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if(not list1 or not list2):
                return list1 if list1 else list2
            l3=None
            curr1=list1
            curr2=list2
            if(list1.val<list2.val):
                l3=list1
                curr1=list1.next
            else:
                l3=list2
                curr2=list2.next
            l3_head=l3
            while True:
                if(not curr1):
                    l3.next=curr2
                    return l3_head
                elif(not curr2):
                    l3.next=curr1
                    return l3_head
                if(curr1.val<curr2.val):
                    l3.next=curr1
                    curr1=curr1.next
                else:
                    l3.next=curr2
                    curr2=curr2.next
                l3=l3.next