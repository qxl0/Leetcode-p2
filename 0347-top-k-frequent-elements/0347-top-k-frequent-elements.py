class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        def countFreq(mid):
            ans = 0
            for x in count.keys():
                if count[x]>=mid:
                    ans += 1
            return ans
        left,right = 0, len(nums)
        while left < right:
            mid = right - (right-left)//2
            if countFreq(mid)>=k:
                # mid is too small
                left = mid
            else:
                right = mid - 1
        f = left
        ans = []
        for x in count.keys():
            if count[x]>=f:
                ans.append(x)
        return ans
