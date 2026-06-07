class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        if self.out:
            return self.out.pop()
        else:
            while self.inp:
                self.out.append(self.inp.pop())
            return self.out.pop()
    
    def peek(self) -> int:
        if self.out:
            return self.out[-1]
        else:
            return self.inp[0]    

    def empty(self) -> bool:
        return False if self.out or self.inp else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()