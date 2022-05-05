class Solution:
    def longestPalindrome(self, s: str) -> str:

        i = len(s)-1
        if s == s[::-1]:
            return s

        while i >= 0:

            for j in range(0, len(s)-i+1):
                substring = s[j:j+i]
                if substring == substring[::-1]:
                    return substring
            i -= 1
            
