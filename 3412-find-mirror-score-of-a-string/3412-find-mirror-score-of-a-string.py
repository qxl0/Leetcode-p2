class Solution:
    def calculateScore(self, s: str) -> int:
        def mirror(ch):
            d = ord(ch)-ord('a')
            return chr(ord('z')-d)
        Map = [[] for _ in range(26)]
        
        ret = 0
        for i,ch in enumerate(s):        
            m = mirror(s[i])
            stack = Map[ord(m)-ord('a')]
            add = False
            while len(stack)>0:
                j = stack.pop()                
                ret += i-j
                add = True
                break
            if not add:
                Map[ord(s[i])-ord('a')].append(i)
        return ret
