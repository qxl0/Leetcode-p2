class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0]*26
        def atoi(ch):
            return ord(ch)-ord('a')
        def itoa(i):
            return chr(ord('a')+i)
        for ch in word:
            freq[atoi(ch)]+=1 
        
        ret = inf
        Set = set(word)
        for c in Set:
            x = freq[atoi(c)]
            # assume c
            cur = 0
            for i in range(26):
                ch = itoa(i)
                y = freq[i] 
                if y<x:
                    cur += y
                elif y>x+k:
                    cur += y-(x+k)
            ret = min(ret, cur)
        return ret 

        
