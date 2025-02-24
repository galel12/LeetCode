class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        start = 0
        maxLen = 0

        for i, char in enumerate(s):
            if char in charMap:
                start = max(start, charMap[char] + 1)
            charMap[char] = i
            maxLen = max(maxLen, i - start + 1)
        return maxLen