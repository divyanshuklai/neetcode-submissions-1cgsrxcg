class Solution:
    def countSubstrings(self, s: str) -> int:
        def manachers(st):
            pst = '#' + '#'.join(st) + '#'
            n = len(pst)
            radius = [0 for _ in range(n)]
            center = 0
            right = 0
            for i in range(n):
                if i < right:
                    radius[i] = min(right - i,  radius[center - ( i - center)])
                else:
                    radius[i] = 0
                
                l , r = i - radius[i], i + radius[i]
                while l >= 0 and r < n and pst[l] == pst[r]:
                    radius[i] += 1
                    l-=1
                    r+=1

            return radius
        
        radius = [r//2 for r in manachers(s)]
        return sum(radius)


# # a # a # a #
# 1 2 3 4 3 2 1
#    1 1 2  1 1