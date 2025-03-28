class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        pal = 0

        for i in range(n):
            #odd palindroms
            l, r = i, i
            while l >= 0 and r <= n - 1 and s[r] == s[l]:
                pal += 1
                l -= 1
                r += 1
                
            #even palindroms
            l, r = i, i + 1
            while l >= 0 and r <= n - 1 and s[r] == s[l]:
                pal += 1
                l -= 1
                r += 1
        
        return pal
