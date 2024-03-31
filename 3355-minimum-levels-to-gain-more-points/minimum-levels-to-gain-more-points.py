class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        temp = []
        for x in possible:
            temp.append(x if x==1 else -1)
        presum = list(accumulate(temp))
        n = len(temp)
        for i in range(n-1):
            if presum[i]>presum[n-1]-presum[i]:
                return i+1
        return -1