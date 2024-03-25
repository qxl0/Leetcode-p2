class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0]*26
        n = len(s)
        ret = 0
        j = 0
        for i,ch in enumerate(s):
            count[ord(ch)-ord('a')] += 1
            while j<i and count[ord(ch)-ord('a')]>2:
                count[ord(s[j])-ord('a')]-=1
                j+=1 
            ret = max(ret, i-j+1)
        return ret 
