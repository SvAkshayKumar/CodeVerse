class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0

        for a, b in zip(s, s[1:]):
            if d[a] < d[b]:
                res -= d[a]
            else:
                res += d[a]
        
        return res + d[s[-1]]