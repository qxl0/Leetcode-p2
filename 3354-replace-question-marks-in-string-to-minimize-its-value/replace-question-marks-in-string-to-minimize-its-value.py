class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = [0]*26
        for ch in s:
            if ch!='?':
                freq[ord(ch)-ord('a')] += 1
        pq = []
        for i in range(26):
            heappush(pq, (freq[i], chr(ord('a') + i) ) )
        
        temp = ''
        for i in range(len(s)):
            if s[i]=='?':
                freq, ch = heappop(pq)
                temp += ch
                heappush(pq,(freq+1,ch))
        temp = ''.join(sorted(temp))
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = temp[j]
                j += 1
        return ''.join(s)