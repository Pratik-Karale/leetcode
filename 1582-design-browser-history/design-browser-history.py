class Node:
    def __init__(self,val,prev,nxt,id):
        self.val=val
        self.prev=prev
        self.next=nxt
        self.id=id
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=Node(homepage,None,None,1)
        self.curr=self.homepage
        self.size=1
    def visit(self, url: str) -> None:
        id=self.curr.id+1
        self.curr.next=Node(url,self.curr,None,id)
        self.size=id
        self.curr=self.curr.next
        print("visitto:",self.curr.val)
    # def move(self,steps):
    #     while steps!=0:
    #         if(steps<0):
    #             self.
    #             steps+=1

    def back(self, steps: int) -> str:
        steps=min(steps,self.curr.id-1)
        for _ in range(self.curr.id,self.curr.id-steps,-1):
            self.curr=self.curr.prev
            print("backto:",self.curr.val)
        return self.curr.val

    def forward(self, steps: int) -> str:
        steps=min(steps,self.size-self.curr.id)
        for _ in range(self.curr.id,self.curr.id+steps,+1):
            self.curr=self.curr.next
            print("forwto:",self.curr.val)
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)