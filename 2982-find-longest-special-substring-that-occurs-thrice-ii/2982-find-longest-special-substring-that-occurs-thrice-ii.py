class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        freq = [[0]*(n+1) for _ in range(26)]
        pre = s[0]
        length = 1
        freq[ord(s[0])-ord('a')][1] = 1
        
        for i in range(1,n):
            cur = s[i]
            if cur == pre:
                length += 1
                freq[ord(cur)-ord('a')][length] += 1
            else:
                freq[ord(cur)-ord('a')][1] += 1
                pre = cur
                length = 1
        ret = -1        
        for i in range(26):
            presum = 0
            for j in range(n,-1,-1):
                presum += freq[i][j]
                if presum>=3:
                    ret = max(ret, j)
                
        return ret 
        