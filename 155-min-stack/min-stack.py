class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, value: int) -> None:
        cm=min(self.arr[-1][1],value) if self.arr else value
        self.arr.append((value,cm))

    def pop(self) -> None:
        return self.arr.pop()[0]

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()