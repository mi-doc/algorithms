class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        if (val := self.stack.pop()) == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = float('inf')
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


if __name__ == "__main__":
    obj = MinStack()

    obj.push(55)
    obj.push(32)
    print(obj.pop())
    print(obj.top())
    obj.push(12)
    obj.push(24)
    print(obj.getMin())



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()