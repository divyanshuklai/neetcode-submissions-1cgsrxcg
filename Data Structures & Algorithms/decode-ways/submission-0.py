class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        mappings = {chr(i): (i - ord("A") + 1) for i in range(ord("A"), ord("Z") + 1)}
        n = len(s)

        totals = [0 for _ in range(n)]
        doubles = [0 for _ in range(n)]

        totals[0] = 1

        for i in range(1, n):
            if s[i] == "0":
                # can only be paired with last 1 or 2, otherwise return 0
                if s[i-1] == "1" or s[i-1] == "2":
                    totals[i] = doubles[i] = (totals[i-1] - doubles[i-1])
                else:
                    return 0
                continue

            totals[i] += totals[i - 1] # count of all patterns with this digit taken alone
            if s[i - 1] == "1" or (s[i - 1] == "2" and int(s[i]) < 7): #count of all patterns with this digit paired with last
                doubles[i] += totals[i - 1] - doubles[i - 1]

            totals[i] += doubles[i]

        return totals[n-1]

    # 20310213
    # 111111
    # 20 3 10 [2 1 | 21]= 2
    # 20 3 10 [2 1 3| 21 3 | 2 13] = 3

    #    1 2 1 2 2 3 1
    # t 1 2 3 5
    # d 0 1 1 2
