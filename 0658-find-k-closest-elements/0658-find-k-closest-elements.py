class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hq = []
        for y in arr:
            heappush(hq, (-abs(y-x), -y))
            if len(hq) > k:
                heappop(hq)
        ret = [-y for _, y in hq]
        return sorted(ret)