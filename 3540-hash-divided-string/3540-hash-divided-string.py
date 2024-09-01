class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        def hashsubstring(str):
            sm = sum(ord(c)-ord('a') for c in str)
            reminder = sm%26
            return chr(reminder+ord('a'))
        hash = [hashsubstring(s[i*k:i*k+k]) for i in range(n//k)]

        return ''.join(hash)
