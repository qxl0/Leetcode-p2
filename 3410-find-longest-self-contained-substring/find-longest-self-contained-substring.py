class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        pre = [[0]*26 for _ in range(n)]
        pre[0][ord(s[0])-ord('a')] = 1
        freq = [0]*26
        left,right = {},{}
        for i in range(n):
            if s[i] not in left:
                left[s[i]] = i    
            right[s[i]] = i     
            freq[ord(s[i])-ord('a')]+=1
            for j in range(26):
                pre[i][j] = pre[i-1][j] + (1 if ord(s[i])-ord('a')==j else 0)

        ans = -1
        for ch in left:
            i = left[ch]
            for ch2 in right:
                j = right[ch2]
                if j==n-1 and i==0 or j<i:
                    continue
                cnt = [0]*26
                valid = True 
                for k in range(26):
                    cnt[k] = pre[j][k]-(pre[i-1][k] if i>0 else 0)
                    if cnt[k]!=0 and cnt[k]!=freq[k]:
                        valid = False
                        break
                if valid:
                    ans = max(ans, j-i+1) 
        return ans   
            
        
        
            