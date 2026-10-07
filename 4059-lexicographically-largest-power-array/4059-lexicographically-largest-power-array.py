class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        N = 15
        res = [0]*N
        done = [0]*N
        grp = [nums]
        for i in range(N):
            bit = 14-i
            grp2 = []
            for g in grp:
                if done[i]:
                    grp2.append(g)
                else:
                    g1 = [a for a in g if a & (1<<bit)]
                    g2 = [a for a in g if not a & (1<<bit)]
                    if g1:
                        res[i] += len(g1)
                        grp2.append(g1)
                    if g2:
                        done[i] = 1
                        grp2.append(g2)
            grp = grp2
        return res
