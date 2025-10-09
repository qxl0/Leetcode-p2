class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        x, freq = count.most_common(1)[0]
        return x