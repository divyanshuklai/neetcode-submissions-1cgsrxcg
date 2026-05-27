class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        padded_string = '#' + '#'.join(s) + '#'
        padlen = len(padded_string)
        
        palstart = 0 
        pallen = 1

        for i in range(padlen):
            left  = i - 1
            right = i + 1
            while left >= 0 and right < padlen and padded_string[left] == padded_string[right]:
                left-=1
                right+=1

            
            thislen = right - left - 1

            if thislen > pallen:
                palstart = left+1
                pallen = thislen
        
        res = ""
        for i in range(palstart, palstart+pallen):
            res += '' if padded_string[i] == '#' else padded_string[i]
        
        print(palstart, pallen)
        return res

# a b b c
# 0 1 2 3 4 5 6 7 8
# # a # b # b # c #


# 0 1 2 3 4 5 6 7 8 9 X 1 
# # a # b # b # a # b # a # b # a # a # b # b # a # a # b # a # 
# 1 3 
