class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = Counter(t)
        total = len(t)
        if len(s)<total:
            return ""
        i = 0
        I,J = 0,-1
        for j in range(len(s)):
            if missing[s[j]]>0:
                total -= 1
            missing[s[j]] -= 1
            if total == 0:
                while missing[s[i]]<0:
                    missing[s[i]] += 1
                    i += 1
                if J<0 or j-i < J-I:
                    I,J = i,j
        return s[I:J+1] if J>=0 else ""
            