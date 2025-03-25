from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {-1 : True}
        memo.update({i : False for i in range(len(s))})
        
        for i in range(len(s)):
            for word in wordDict:
                if(i - len(word) + 1 >= 0 and s[i - len(word) + 1: i + 1] == word):
                    memo[i] = memo[i - len(word)]
                if memo[i]:
                    break

        res = memo[len(s) - 1]
        return res