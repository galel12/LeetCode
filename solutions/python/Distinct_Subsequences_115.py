class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if(len(s) < len(t)):
            return 0

        def dfs(i, j):
            if j == len(t):
                return 1 if i <= len(s) else 0
            
            ans = 0 
            if i < len(s) and s[i] == t[j]:
                ans += dfs(i + 1, j + 1) + dfs(i + 1, j)
                
            if i < len(s) and s[i] != t[j]:
                ans += dfs(i + 1, j)
            return ans
        
        res = dfs(0, 0)
        return res
            