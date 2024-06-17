class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        A = sorted(set(rewardValues))
        b = 1<<0  # stands for 0 in rewards
        for a in A[:-1]:
            b |= (b&((1<<a)-1))<<a
        # check b for 1 before a
        pos=0
        for i in range(A[-1]-1,-1,-1):
            if (b>>i)&1==1:
                pos = i
                break
        return A[-1]+pos
