class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] 
        self.min = float('inf')
    def push(self, val: int) -> None:
        if val <= self.min: 
            self.min = val 
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            self.minStack.pop()
            self.min = self.minStack[-1] if self.minStack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
