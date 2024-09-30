class Solution:
    def countOfSubstrings(self, s: str, k: int) -> int:        
        n = len(s)
        ret = 0
        for i in range(n):          
            a,e,m,o,u = 0,0,0,0,0
            c = 0
            for j in range(i,n):
                if s[j]=='a': a += 1
                elif s[j]=='e': e +=1
                elif s[j]=='i': m +=1
                elif s[j]=='o': o +=1
                elif s[j]=='u': u +=1
                else: c += 1
                if a and e and m and o and u and c==k:
                    ret += 1
        return ret
