class MinStack:

    def __init__(self):
        # self.minVal = float("inf")
        self.stack = []
        self.minPre = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.minVal = min(self.minVal, val)
        if self.minPre:
            self.minPre.append(min(self.minPre[-1], val))
        else:
            self.minPre.append(val)
    def pop(self) -> None:
        self.minPre.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minPre[-1]
