class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, value: int) -> None:
        # If stack has items, compare with the current top's minimum.
        # Otherwise, the value itself is the minimum.
        current_min = min(value, self.arr[-1][1]) if self.arr else value
        self.arr.append((value, current_min))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]