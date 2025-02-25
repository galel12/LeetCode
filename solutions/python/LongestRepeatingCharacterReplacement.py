class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = 0
        maxLength = 0
        start = 0
        
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)    # count the frequency of each character 
            maxFreq = max(maxFreq, count[s[end]])       # update the maximum frequency of a character

            """
            If the number of replacements needed to make the substring
            from start to end inclusive have more than k replacements,
            we need to shrink the window    
            """      
            if (end - start + 1) - maxFreq > k:
                count[s[start]] -= 1    # decrement the character frequency at the start of the window
                start += 1 
            
            maxLength = max(maxLength, end - start + 1) 
            
        return maxLength