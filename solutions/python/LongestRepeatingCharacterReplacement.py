class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxCount = 0
        maxLength = 0
        start = 0
        
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            maxCount = max(maxCount, count[s[end]])

            # If the number of replacements needed to make the substring
            # from start to end inclusive have more than k replacements,
            # we need to shrink the window           
            if (end - start + 1) - maxCount > k:
                count[s[start]] -= 1 # Remove the character at the start of the window
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
            
        return maxLength