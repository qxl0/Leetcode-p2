class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        set1,set2 = set(nums1),set(nums2)
        both = set1&set2
        only1,only2 = set1-both,set2-both
        return min(n, min(n//2,len(only1))+min(n//2,len(only2))+len(both))