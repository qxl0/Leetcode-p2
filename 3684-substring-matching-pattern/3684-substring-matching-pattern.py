class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        x = p.find('*')
        p1 = p[:x]
        p2 = p[x+1:]
        i = s.find(p1)
        j = s.rfind(p2)
        if i != -1 and j!=-1 and i+len(p1)<=j:
            return True
        return False

