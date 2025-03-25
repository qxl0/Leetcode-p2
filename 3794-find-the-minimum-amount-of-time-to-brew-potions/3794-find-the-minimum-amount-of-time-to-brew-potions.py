class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        acc = list(accumulate(skill))
        m = len(mana)
        t = 0
        t2 = 0
        for i in range(1, m):
            for j in range(n-1,-1,-1):
                finish = t + mana[i-1]*acc[j]
                t2 = max(t2, finish-mana[i]*(acc[j-1] if j>0 else 0))
            # 
            t = t2
        # to last mana[m-1]
        return t + acc[n-1]*mana[m-1]

