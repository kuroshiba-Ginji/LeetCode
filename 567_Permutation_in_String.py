class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = ''.join(sorted(s1))
        #for i in range(len(s2)-len(s1)+1):
        #    substring = s2[i:i+len(s1)]
        #    substring = ''.join(sorted(substring))
        #    if substring == s1:
        #        return True

        #return False

        window = len(s1)
        s1_c = Counter(s1)

        for i in range(len(s2)-window+1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True

        return False
            
