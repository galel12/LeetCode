class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s, hashmap_t = {},{} # char : num of duplicates in string
        
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i],0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i],0)

        return hashmap_s == hashmap_t
