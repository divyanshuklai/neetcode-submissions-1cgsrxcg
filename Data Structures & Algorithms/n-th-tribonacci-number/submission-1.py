class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 1:
            return 0
        if n < 3:
            return 1
        
        fibo = [0 for _ in range(n+1)]

        fibo[0] = 0
        fibo[1] = fibo[2] = 1

        for i in range(3, n+1):
            fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3]

        return fibo[n]