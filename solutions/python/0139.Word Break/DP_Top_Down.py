from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {-1 : True}
        
        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if(i - len(word) + 1 < 0):
                    continue
                if s[i - len(word) + 1 : i + 1] == word:
                    if(dfs(i - len(word))):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        res = dfs(len(s) - 1)
        return res