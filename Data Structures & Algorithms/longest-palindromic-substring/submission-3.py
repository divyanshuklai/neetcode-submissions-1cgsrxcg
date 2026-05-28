class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher's algo
        ps = '#' + '#'.join(s) + '#'
        n = len(ps)

        radius = [0 for _ in range(n)]
        center = 0
        right = 0
        for i in range(n):
            if i < right:
                radius[i] =  min(
                    right - i,
                    radius[2 * center - i]
                )
            else:
                radius[i] = 0
            l, r = i-radius[i], i+radius[i]
            while l >= 0 and r < n and ps[l] == ps[r]:
                radius[i]+=1
                l-=1
                r+=1
            if i + radius[i] > right:
                center = i
                right = i + radius[i] 
        
        cen, rad = max(enumerate(radius), key=lambda x : x[1])
        start = cen - rad
        res = ""
        for i in range(start+1, start+2*rad):
            res += "" if ps[i] == "#" else ps[i]
        return res
