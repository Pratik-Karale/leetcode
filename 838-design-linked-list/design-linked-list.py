class Node:
    def __init__(self,val=None,nxt=None):
        self.val=val
        self.next=nxt
class MyLinkedList:
    def print_ll(func):
        def wrapper(self, *args, **kwargs):
            print("--- Before the method call ---")
            result = func(self, *args, **kwargs) 
            print(func.__name__,*args, **kwargs)
            curr=self.temp_head
            while curr:
                print(curr.val,end=", ")
                curr=curr.next
            print()
            print("tmp: ",self.temp_head.val)
            if(self.head):
                print("hed: ",self.head.val)
            print("sz:",self.size)
            print("--- After the method call ---")
            return result
        return wrapper

    def __init__(self):
        self.temp_head=Node()
        self.head=None
        self.size=0
    # @print_ll
    def get(self, index: int) -> int:
        if(index>=self.size):
            return -1
        if(index<0):
            index=0
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val
    # @print_ll
    def addAtHead(self, val: int) -> None:
        n=Node(val,self.head)
        self.head=n
        self.temp_head.next=n
        self.size+=1
    # @print_ll
    def addAtTail(self, val: int) -> None:
        curr=self.temp_head
        while curr.next:
            curr=curr.next
        curr.next=Node(val)
        if self.size==0:
            self.head=curr.next
            self.temp_head.next=self.head
        self.size+=1

    # @print_ll
    def addAtIndex(self, index: int, val: int) -> None:
        if(index>self.size):
            return -1
        if(index<0):
            index=0
        curr=self.head
        prev=self.temp_head
        for i in range(index):
            prev=curr
            curr=curr.next
        prev.next=Node(val)
        prev.next.next=curr
        
        if index==0:
            self.head=prev.next
            self.temp_head.next=self.head
        self.size+=1
        
    # @print_ll
    def deleteAtIndex(self, index: int) -> None:
        if(index>=self.size):
            return -1
        if(index<0):
            index=0
        curr=self.head
        prev=self.temp_head
        for i in range(index):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        if(index==0):
            self.head=curr.next
        # if index==0:
        #     self.head=None
        #     self.temp_head.next=self.head
        # if(not curr):
        #     prev.next=None
        #     self.temp_head=None
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)