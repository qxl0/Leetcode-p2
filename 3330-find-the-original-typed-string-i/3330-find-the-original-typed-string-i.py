class Solution:
    def possibleStringCount(self, word: str) -> int:        
        ret = 1
        n = len(word)
        i = 0
        while i<n:
            freq = 1
            j = i+1
            while j<n and word[j]==word[i]:
                j += 1
                freq += 1
            # when stop  j-> 
            ret += freq-1
            i = j
        return ret