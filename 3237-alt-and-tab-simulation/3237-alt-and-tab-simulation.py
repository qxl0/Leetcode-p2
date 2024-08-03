class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        ret = []
        seen = set()
        for q in queries[::-1]:
            if q not in seen:
                seen.add(q)
                ret.append(q)
        for x in windows:
            if x not in seen:
                ret.append(x)
        return ret
