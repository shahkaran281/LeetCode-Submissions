class MyQueue:

    def __init__(self):
        self.forward = []
        self.backward = []

    def push(self, x: int) -> None:
        self.forward.append(x)

    def pop(self) -> int:
        while len(self.forward) != 0:
            self.backward.append(self.forward.pop())
        x = self.backward.pop()
        while len(self.backward) != 0:
            self.forward.append(self.backward.pop())
        return x

    def peek(self) -> int:
        if len(self.forward) == 0:
            return None
        while len(self.forward) != 0:
            self.backward.append(self.forward.pop())
        x = self.backward[-1]
        while len(self.backward) != 0:
            self.forward.append(self.backward.pop())
        return x
            

    def empty(self) -> bool:
        return len(self.forward) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()