class MinStack:

    def __init__(self):
        self.st = []
        self.a = []

    def push(self, val: int) -> None:
        if self.st:
            self.st.append(val)
            if val <= self.a[-1]:
                self.a.append(val)
        else:
            self.st.append(val)
            self.a.append(val)

    def pop(self) -> None:
        x = self.st.pop()
        if x==self.a[-1]:
            self.a.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.a[-1]
