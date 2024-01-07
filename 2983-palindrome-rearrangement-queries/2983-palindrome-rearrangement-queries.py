class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        psd = [0]
        i,j = 0,n-1
        while i<j:
            psd.append( psd[-1] + (s[i]!=s[j]))
            i += 1
            j -= 1
        psc = []
        psc.append([0]*26)
        for i in range(n):
            cnt = psc[-1].copy()
            ch = ord(s[i])-ord('a')
            cnt[ch] += 1
            psc.append(cnt)
        def isPositive(cnt):
            return all(c>=0 for c in cnt)
        def isEqual(cnt1, cnt2):
            return all(c1==c2 for c1,c2 in zip(cnt1,cnt2))
        def sub(cnt1, cnt2):
            return [c1-c2 for c1,c2 in zip(cnt1,cnt2)]
        # now let's tacke the queries
        ans = []
        for a1,b1,c1,d1 in queries:
            # change to left close, right open
            b1,d1 = b1+1,d1+1
            # find mirror
            a2 = n-a1
            b2 = n-b1
            c2 = n-c1
            d2 = n-d1
            if min(a1,d2)!=0 and psd[min(a1,d2)]!=0 or max(b1,c2)<n//2 and (psd[n//2] - psd[max(b1,c2)]!=0) or b1<d2 and (psd[d2]-psd[b1]!=0) or a1>c2 and (psd[a1]-psd[c2]!=0):
                ans.append(False)
            else:
                ix1 = sub(psc[d1],psc[c1])
                ix2 = sub(psc[b1],psc[a1])
                if a1>d2:
                    ix1 = sub(ix1, sub(psc[min(a1,c2)],psc[d2]))
                if c2>b1:
                    ix1 = sub(ix1, sub(psc[c2], psc[max(b1,d2)]))
                if c1>b2:
                    ix2 = sub(ix2, sub(psc[min(a2,c1)], psc[b2]))
                if a2>d1:
                    ix2 = sub(ix2, sub(psc[a2], psc[max(b2,d1)]))
                # check ix1 ix2
                if isPositive(ix1) and isPositive(ix2) and isEqual(ix1,ix2):
                    ans.append(True)
                else:
                    ans.append(False)
        return ans 
               
            
            