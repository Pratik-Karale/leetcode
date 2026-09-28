from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
    def push(self, x: int) -> None:
        print("f")
        self.q.append(x)
        self.t=x
    def pop(self) -> int:
        # print("sddsfddd")
        for _ in range(len(self.q)-1):
            fr=self.q.popleft()
            self.q.append(fr)
            self.t=fr
        popped=self.q.popleft()
        # if(self.q):
        # if self.q:
        # else:
        #     self.t=-1
        # else:
        #     -1
        return popped 

    def top(self) -> int:

        # print("sfffdzzzddsf")
        return self.t

    def empty(self) -> bool:
        # print("sddsf")
        print(len(self.q))
        return True if not len(self.q) else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()