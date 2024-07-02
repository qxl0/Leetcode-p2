class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map2 = Counter(nums2)
        ret = []
        for x in nums1:
            if x not in Map2: 
                continue
            ret.append(x)
            Map2[x] -= 1
            if Map2[x]==0:
                del Map2[x]
        return ret 