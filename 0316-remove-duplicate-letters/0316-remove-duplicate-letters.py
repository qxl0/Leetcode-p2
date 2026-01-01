class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        lastpos = {ch:i for i,ch in enumerate(s)}
        print(lastpos)
        seen = {}
        ret = []
        for i,ch in enumerate(s):
            if ch in seen and seen[ch]: continue
            while ret and ret[-1]>ch and lastpos[ret[-1]]>i:
                seen[ret[-1]] = False
                ret.pop()
            
            ret.append(ch)
            seen[ch] = True
        return "".join(ret)
# cbacdcbc "acdb"
# 0      
# n = len(s) = 8
# lastpos:
# c: 4, 7
# b: 2, 6
# a: 1, 2
# d: 1, 4

# a c d b  

