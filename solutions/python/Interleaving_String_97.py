from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if(len(s3) != m + n):
            return False

        @lru_cache(None)
        def dfs(i, j, k):
            if k == len(s3):
                return True

            if i < len(s1) and s1[i] == s3[k]:
                if(dfs(i + 1, j, k + 1)):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if(dfs(i, j + 1, k + 1)):
                    return True
            return False

        return dfs(0, 0, 0)