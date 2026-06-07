class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        for sym in s:
            if sym in "([{":
                par.append(sym)
            elif par:
                if sym==")" and par[-1]=="(":
                    par.pop()
                elif sym=="]" and par[-1]=="[":
                    par.pop()
                elif sym=="}" and par[-1]=="{":
                    par.pop()
                else:
                    return False
            else:
                return False
        if not par:
            return True
        return False
                