class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k==0: return s
        def dist(ch, ch0):
            d = ord(ch)-ord(ch0)     
            if d>13:
                d = 26-d  
            return d     
        def moveleft(ch, p):  # move p positions             
            return chr(ord(ch)-p)
        ans = list(s)
        for i,ch in enumerate(s):
            if dist(ch,'a')<=k:
                ans[i] = 'a'
                k -= dist(ch,'a')
            else:
                ans[i] = moveleft(ch,k) 
                break   
        return "".join(ans)