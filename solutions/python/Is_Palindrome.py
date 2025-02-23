
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for char in s:
            if char.isalnum():
                pal += char.lower()
        return pal == pal[::-1]


