class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        j = 0
        for i,ch in enumerate(s2):
            c2[ch] += 1
            while c2 > c1 and j<len(s2):
                c2[s2[j]] -= 1
                if c2[s2[j]] == 0:
                    del c2[s2[j]]
                j += 1
            if c1 == c2:
                return True
        return False