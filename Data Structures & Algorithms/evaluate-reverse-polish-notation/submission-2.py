class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        for tok in tokens:
            if tok == "+":
                vals.append(vals.pop() + vals.pop())
            elif tok=="-" and len(tok)==1:
                b = vals.pop()
                a = vals.pop()
                vals.append(a - b)
            elif tok=="*":
                vals.append(vals.pop() * vals.pop())
            elif tok=="/":
                b = vals.pop()
                a = vals.pop()
                vals.append(int(a/b))
            else:
                vals.append(int(tok))
        return vals[0]
