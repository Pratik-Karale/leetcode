# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        curr=dummy
        while(list1 or list2):
            if(not list1):
                curr.next=list2
                break
            elif(not list2):
                curr.next=list1
                break

            if(list1.val<=list2.val):
                curr.next=list1
                list1=list1.next
                curr=curr.next
            elif(list2):
                curr.next=list2
                list2=list2.next
                curr=curr.next
        return dummy.next
            
            
        