class MyStack:

    def __init__(self):
        self.main = []

    def push(self, x: int) -> None:
        n = len(self.main)
        self.main.append(x)
        for _ in range(n):
            self.main.append(self.main.pop(0))

    def pop(self) -> int:
        return self.main.pop(0)

    def top(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return False if self.main else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()