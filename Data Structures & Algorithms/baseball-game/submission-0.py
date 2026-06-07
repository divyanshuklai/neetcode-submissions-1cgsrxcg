class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                a = record[-1]
                b = record[-2]
                record.append(a + b)
            elif op=="D":
                record.append(record[-1] * 2)
            elif op=="C":
                record.pop()
            else:
                record.append(int(op))
        
        return sum(record)