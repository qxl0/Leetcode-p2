class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m,n = len(s1),len(s2)
        s1 = '#'+s1
        s2 = '#'+s2

        next = [[-1]*26 for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            next[i] = next[i+1].copy()
            next[i][ord(s1[i+1])-ord('a')] = i+1
        start = [i for i in range(1,m+1) if s1[i]==s2[1]]

        ret = ""
        for i in start:
            j = i-1
            flag = 1
            for ch in s2[1:]:
                # print(j, ord(ch)-ord('a'), ch)
                j = next[j][ord(ch)-ord('a')]
                if j == -1:
                    flag = 0
                    break
            if flag == 1:
                if ret=="" or j-i+1<len(ret):
                    ret = s1[i:j+1]
                
        return ret