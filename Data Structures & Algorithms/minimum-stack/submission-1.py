class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = float("-inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currMin = min(self.currMin, val)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
