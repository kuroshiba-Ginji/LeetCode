class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        string = ''

        for l in s:
            if l in string:
                longest = max(longest, len(string))
                string = string[string.index(l)+1:]
            string += l
        longest = max(longest, len(string))
        return longest
