class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ret = 1
        for x in sorted(count.keys(), reverse=True): 
            if x==1: 
                ret = max(ret, count[x])
                continue
            if not sqrt(x).is_integer():continue
            y = int(sqrt(x))
            k = 0
            while y in count and count[y]>=2:
                k += 1
                if not sqrt(y).is_integer(): break
                y = int(sqrt(y))
            ret = max(ret, 1+k*2)
        if ret%2==0: ret -= 1
        return ret