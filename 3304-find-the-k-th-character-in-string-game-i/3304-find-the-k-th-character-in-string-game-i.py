class Solution:
    def kthCharacter(self, k: int) -> str:
        def nextch(c):
            v = (ord(c)+1-ord('a'))%26
            return chr(v+ord('a'))
        initial = 'a'
        cur = initial
        while len(cur)<k:
            next = ''.join([nextch(ch) for ch in cur])
            cur += next 
        return cur[k-1]